from rest_framework import serializers

from kioskController.models import PCParentOrganization, PCParentOrganizationPhone,\
PCParentOrganizationAddress, PCParentOrganizationEmail


class PCParentOrganizationPhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = PCParentOrganizationPhone
        fields = '__all__'


class PCParentOrganizationAddressSerializer(serializers.ModelSerializer):

    class Meta:
        models = PCParentOrganizationAddress
        fields = '__all__'


class PCParentOrganizationEmailSerializer(serializers.ModelSerializer):

    class Meta:
        models = PCParentOrganizationEmail
        fields = '__all__'


class PCParentOrganizationSerializer(serializers.ModelSerializer):

    phones = serializers.SerializerMethodField('get_phones')
    address = serializers.SerializerMethodField('get_address')
    emails = serializers.SerializerMethodField('get_emails')

    def get_phones(self, obj: PCParentOrganization):
        """Получить телефоны вышестоящий организации"""
        phones = PCParentOrganizationPhone.objects.filter(
            org=obj
        )

        return PCParentOrganizationPhoneSerializer(phones, many=True).data
    

    def get_address(self, obj: PCParentOrganization):
        """Получить адресса вышестоящий организации"""
        address = PCParentOrganizationAddress.objects.filter(
            org=obj
        )

        return PCParentOrganizationAddressSerializer(address, many=True).data
    
    def get_emails(self, obj: PCParentOrganization):
        """Получить emails вышестоящий оргнизации"""
        emails = PCParentOrganizationEmail.objects.filter(
            org=obj
        )
        return PCParentOrganizationEmailSerializer(emails, many=True).data


    class Meta:
        model = PCParentOrganization
        fields = [
            'id',
            'name',
            'phones',
            'address',
            'emails'
        ]