import datetime
import xml.etree.ElementTree as ET
import re

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.filters import OrderingFilter
import requests

from pre_registration.models import PreRegistration, PreRegistrationLog, PreRegistrationRecord
from pre_registration.serializer import PreRegistrationSerializer, PreRegistrationRecordSerializer


def get_all_values_by_id(xml_str, target_id):
    """
    Возвращает первое значение Value для заданного ID
    """
    root = ET.fromstring(xml_str)
    
    for record in root.findall('.//Record'):
        record_id = record.find('Id').text.strip()
        
        if record_id == target_id:
            # Берем первый Item и его Value
            first_item = record.find('.//Item')
            if first_item is not None:
                value_elem = first_item.find('Value')
                if value_elem is not None and value_elem.text:
                    return value_elem.text.strip()
    return ""

class PreRegistrationViewSet(viewsets.ModelViewSet):
    queryset = PreRegistration.objects.all()
    serializer_class = PreRegistrationSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['prioritet']
    ordering = ['prioritet']


    def get_serializer_class(self):

        if self.action == 'make_recording':
            return PreRegistrationRecordSerializer
        else:
            return PreRegistrationSerializer


    def destroy(self, request, *args, **kwargs):
        return Response(
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    
    def create(self, request, *args, **kwargs):
        return Response(
            status=status.HTTP_405_METHOD_NOT_ALLOWED   
        )
    
    def update(self, request, *args, **kwargs):
        return Response(
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    
    @action(detail=True, methods=['GET'])
    def check_online(self, req: Request, pk=None):
        """Проверить находится ли сервер очереди в онлайне"""
        pre_reg = get_object_or_404(PreRegistration, pk=pk)

        try: 
            res = requests.get(
                url=f'http://{pre_reg.ip_addr}:{pre_reg.port}',
                timeout=2
            )

            if res.status_code != 200:

                PreRegistrationLog.objects.create(
                    pre_registration=pre_reg,
                    error=True,
                    content=f'Ответ от сервера очереди {res.status_code}: {res.text}'
                )

                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        'online': False
                    }
                )

            else:
                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        'online': True
                    }
                )

        except Exception as ex:

            return Response(
                status=status.HTTP_200_OK,
                data={
                    'online': False
                }
            )
    
    @action(detail=True, methods=['GET'])
    def get_available_date_for_preregistration(self, req: Request, pk=None):
        """Получить доступные даты с пререгистрации"""

        pre_reg = get_object_or_404(PreRegistration, pk=pk)

        today = datetime.date.today()

        start_date = today.strftime('%d.%m.%Y')

        end_date = (today + datetime.timedelta(days=30)).strftime('%d.%m.%Y')

        try:
            res = requests.post(
                url=f'http://{pre_reg.ip_addr}:{pre_reg.port}',
                headers={
                    'Content-Type': 'application/xml'
                },
                data=f"""
    <Request>
        <Component>General</Component>
        <Command>SelectAvailableTimes</Command>
        <Branch>{pre_reg.czn_code}</Branch>
        <ServiceId>{pre_reg.pre_registration_code}</ServiceId>
        <DateFrom>{start_date}</DateFrom>
        <DateTo>{end_date}</DateTo>
    </Request>
    """
            )

            if res.status_code != 200:
                PreRegistrationLog.objects.create(
                    pre_registration=pre_reg,
                    error=True,
                    content=f'Ответ от сервера очереди {res.status_code}: {res.text}'
                )

                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={
                        'detail': res.text
                    }
                )
            else:
                return Response(
                    status=status.HTTP_200_OK,
                    headers={
                        'Content-Type': 'application/xml'
                    },
                    data=res.text
                )

        except Exception as ex:
            PreRegistrationLog.objects.create(
                pre_registration=pre_reg,
                error=True,
                content=str(ex)
            )

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'detail': str(ex)
                }
            )
        
    
    @action(detail=False, methods=['POST'])
    def make_recording(self, req: Request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=req.data)

        if serializer.is_valid():
            pre_reg = serializer.validated_data.get('pre_registration')

            selected_date = serializer.validated_data.get('date_time').strftime('%d.%m.%Y %H:%M')
            date_for_get_code = serializer.validated_data.get('date_time').strftime('%d.%m.%Y')
            try:
                res = requests.post(
                    url=f'http://{pre_reg.ip_addr}:{pre_reg.port}',
                    headers={
                        'Content-Type': 'application/xml'
                    },
                    data=f"""
<Request>
    <Component>General</Component>
    <Command>Preregister</Command>
    <Branch>{pre_reg.czn_code}</Branch>
    <ServiceId>{pre_reg.pre_registration_code}</ServiceId>
    <PreregistrationDateTime>{selected_date}</PreregistrationDateTime>
    <UpdateByActivationCode></UpdateByActivationCode>
    <UpdateByImportCode></UpdateByImportCode>
    <ExtraData></ExtraData>
</Request>
"""
                )

                if res.status_code != 200:

                    PreRegistrationLog.objects.create(
                        pre_registration=pre_reg,
                        error=True,
                        content=f'Ответ от сервера очереди {res.status_code}: {res.text}'
                    )

                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={
                            'detail': res.text
                        }
                    )
                
                else:

                    match = re.search(r'<PreregistrationId>(.*?)</PreregistrationId>', res.text, re.DOTALL)
                    if match:
                        code = match.group(1).strip() #Получили код который хранится в базе

                        # Делаем запрос, чтобы получить код для пользователя
                        res_for_code = requests.post(
                            url=f'http://{pre_reg.ip_addr}:{pre_reg.port}',
                            headers={
                                'Content-Type': 'application/xml'
                            },
                            data=f"""
    <Request>
    <Component>General</Component>
    <Command>SelectPreregistrations</Command>
    <Branch>{pre_reg.czn_code}</Branch>
    <DateFrom>{date_for_get_code}</DateFrom>
    <DateTo>{date_for_get_code}</DateTo>
    <ExtraDataFieldNumber/>
    <ExtraDataFieldValue/>
    </Request>
    """
                        )

                        if res_for_code.status_code != 200:
                            PreRegistrationLog.objects.create(
                                pre_registration=pre_reg,
                                error=True,
                                content=f'Ответ от сервера очереди {res.status_code}: {res.text}'
                            )
                            return Response(
                                    status=status.HTTP_400_BAD_REQUEST,
                                    data={
                                        'detail': res.text
                                    }
                            )
                        else:
                 
                            code_pre_reg = get_all_values_by_id(res_for_code.text, code)

                            if code_pre_reg:
                                return Response(
                                    status=status.HTTP_200_OK,
                                    data={
                                        'code': code_pre_reg
                                    }
                                )
                            else:
                                return Response(
                                    status.HTTP_400_BAD_REQUEST,
                                    data={
                                        'detail': 'not found code'
                                    }
                                )

                    else:
                        return Response(
                            status=status.HTTP_400_BAD_REQUEST,
                            data={
                                'detail': 'can`t get code from pre-reg'
                            }
                        )

            except Exception as ex:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={
                        'detail': str(ex)
                    }
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )