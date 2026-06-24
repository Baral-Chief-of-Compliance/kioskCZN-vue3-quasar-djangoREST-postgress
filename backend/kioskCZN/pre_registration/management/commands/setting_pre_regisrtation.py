from django.core.management.base import BaseCommand, CommandError

from pre_registration.models import PreRegistration


PRE_REGISTRATIONS = [
    {
        'name': 'Кандалакша',
        'ip_addr': '172.25.0.201',
        'port': 21350,
        'show': True,
        'pre_registration_code': '{342153C6-F5D3-11EE-BFBC-A8A159F73B56}',
        'czn_code': 'czn_kanda',
        'prioritet': 999,
        'address': '184040, Мурманская область, г. Кандалакша, ул. Пронина, д. 22А'
    },
    {
        'name': 'Полярные зори',
        'ip_addr': '172.25.2.201',
        'port': 21350,
        'show': True,
        'pre_registration_code': '{10F972A8-6075-11EF-BFE0-A8A159F73B88}',
        'czn_code': 'czn_pz',
        'prioritet': 999,
        'address': '184230, Мурманская область, г. Полярные Зори, пр-т Нивский, д.11'
    },
    {
        'name': 'Мончегорск',
        'ip_addr': '172.25.4.201',
        'port': 21350,
        'show': True,
        'pre_registration_code': '{944089B8-F649-11EE-BFDE-A8A159F73B67}',
        'czn_code': 'czn_moncha',
        'prioritet': 999,
        'address': '184511, Мурманская область, г.Мончегорск, ул. Нюдовская, д.16'
    },
    {
        'name': 'Оленегорск',
        'ip_addr': '172.25.6.201',
        'port': 21350,
        'show': True,
        'pre_registration_code': '{D599378B-75CD-11EF-BFE9-A8A159F47650}',
        'czn_code': 'czn_olen',
        'prioritet': 999,
        'address': '184530, Мурманская область, г. Оленегорск, ул.Строительная, д. 59'
    },
    {
        'name': 'Ковдор',
        'ip_addr': '172.25.8.201',
        'port': 21350,
        'show': True,
        'pre_registration_code': '{923B22EA-97D6-11F0-803D-74563C96BAB8}',
        'czn_code': 'czn_kovdor',
        'prioritet': 999,
        'address': '184140, Мурманская область, г. Ковдор, ул. Кирова, д.19'
    },
    {
        'name': 'Североморск',
        'ip_addr': '172.25.12.201',
        'port': 21350,
        'show': True,
        'pre_registration_code': '{3DFDA345-7692-11EF-BFC6-A8A159F72D51}',
        'czn_code': 'czn_severomorsk',
        'prioritet': 999,
        'address': '184600, Мурманская область, г. Североморск, ул.Корабельная, д.2'
    },
    {
        'name': 'Мурманск',
        'ip_addr': '172.25.31.1',
        'port': 21350,
        'show': True,
        'pre_registration_code': '{16A958B7-F35F-11EE-BBB2-000C291571B5}',
        'czn_code': 'czn_murmansk',
        'prioritet': 1,
        'address': '183039, г. Мурманск, ул. Академика Книповича, д.48'
    },
]

class Command(BaseCommand):
    help = 'add base pre-registration in database'

    def handle(self, *args, **options):
        for pr in PRE_REGISTRATIONS:
            try:
                PreRegistration.objects.get(
                    czn_code=pr['czn_code']
                )
            except PreRegistration.DoesNotExist:
                PreRegistration.objects.create(
                    name=pr['name'],
                    show=pr['show'],
                    pre_registration_code=pr['pre_registration_code'],
                    czn_code=pr['czn_code'],
                    ip_addr=pr['ip_addr'],
                    port=pr['port'],
                    address=pr['address']
                )

                self.stdout.write(
                    self.style.SUCCESS('Successfully created pre_registration "%s"' % pr['name'])
                )

            except PreRegistration.MultipleObjectsReturned:
                pass