from rest_framework import serializers

from kioskController.models import PC, PCSocialNetworks, PCAddress,\
PCPhone, PCEmail, PCSites, PCTimeTable, PCHeadInfo,\
PCHeadInfoPhone, PCHeadInfoEmail, PCHeadInfoTimeTable


class PCSerializer(serializers.ModelSerializer):

    class Meta:
        model = PC
        fields = '__all__'


class PCDetailSerializer(serializers.ModelSerializer):
    """Серириализатор для детальной информации о кадровом центре"""

    social_networks = serializers.SerializerMethodField(
        'get_social_networks'
    )
    address = serializers.SerializerMethodField(
        'get_address'
    )
    phones = serializers.SerializerMethodField(
        'get_phones'
    )
    emails = serializers.SerializerMethodField(
        'get_emails'
    )
    sites = serializers.SerializerMethodField(
        'get_sites'
    )
    timetables = serializers.SerializerMethodField(
        'get_timetables'
    )

    head_info = serializers.SerializerMethodField(
        'get_head_info'
    )

    def get_social_networks(self, obj: PC):
        """Получить список социальных сетей КЦ"""
        pass

    def get_address(self, obj: PC):
        """Получить адресс кадрового центра"""
        addresses = PCAddress.objects.filter(
            pc=obj
        ).order_by("priority")

        results = []

        for adr in addresses:
            results.append(
                {
                    "address": adr.address
                }
            )

        return results
    
    def get_phones(self, obj: PC):
        """Получить телефоны КЦ"""
        phones = PCPhone.objects.filter(
            pc=obj
        ).order_by("priority")

        results = []

        for ph in phones:
            results.append(
                {
                    "name": ph.name,
                    "phone": ph.phone
                }
            )
        return results
    
    def get_emails(self, obj: PC):
        """Получить email кадрового центра"""
        emails = PCEmail.objects.filter(
            pc=obj
        ).order_by("priority")

        results = []

        for e in emails:
            results.append(
                {
                    'name': e.name,
                    'email': e.email
                }
            )

        return results
    
    def get_sites(self, obj: PC):
        """Получить сайты кадрового центра"""
        sites = PCSites.objects.filter(
            pc=obj
        ).order_by("priority")

        results = []

        for s in sites:
            results.append(
                {
                    'name': s.name,
                    'url': s.url,
                    'qr_code_img': s.qr_code_img.url
                }
            )

        return results
    
    def get_timetables(self, obj: PC):
        """Получить расписание кадрового центра"""
        time_tables = PCTimeTable.objects.filter(
            pc=obj
        ).order_by("day_of_week")

        results = []

        for tt in time_tables:
            results.append(
                {
                    'day_of_week': tt.day_of_week,
                    'day_off': tt.day_off,
                    'time_start': tt.time_start,
                    'time_end': tt.time_end
                }
            )

        return results
    
    def get_head_info(self, obj: PC):
        """Получить инциформацию о главе кадрового центра"""
        # Информация о главе кадрового центра
        head_info_pc = PCHeadInfo.objects.filter(
            pc=obj
        ).first()

        # Информация о главе управляющего кадрового центра
        head_info_pc_main = PCHeadInfo.objects.filter(
            pc__main=True
        ).first()

        results = {
            "head_worker" : None,
            "head_name": None,
            "head_photo": None,
            "main_head_worker": None,
            "main_head_name": None,
            "main_head_photo": None
        }

        if head_info_pc:
            if head_info_pc.worker:
                results['head_worker'] = head_info_pc.worker.fio
            results['head_name'] = head_info_pc.name
            if head_info_pc.photo:
                results['head_photo'] = head_info_pc.photo.url

        if head_info_pc_main:
            if head_info_pc_main.worker:
                results["main_head_worker"] = head_info_pc_main.worker.fio
            results["main_head_name"] = head_info_pc_main.name
            if head_info_pc_main.photo:
                results["main_head_photo"] = head_info_pc_main.photo.url

        return results

    class Meta:
        model = PC
        fields = [
            "id",
            "name",
            "social_networks",
            "address",
            "phones",
            "emails",
            "sites",
            "timetables",
            "head_info"
        ]