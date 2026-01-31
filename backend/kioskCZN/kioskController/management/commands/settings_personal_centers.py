from django.core.management.base import BaseCommand, CommandError

from kioskController.models import PC


PCS = [
    {
        'name': 'Управляющий',
        'url_path': 'сontrol',
        'id_parsing': 1
    },
    {
        'name': 'Мурманский',
        'url_path': 'murmansk',
        'id_parsing': 2
    },
    {
        'name': 'Кандалакшский',
        'url_path': 'kandalaksha',
        'id_parsing': 3
    },
    {
        'name': 'Полярнозоринский',
        'url_path': 'polyarnozorinsky',
        'id_parsing': 4
    },
    {
        'name': 'Терский',
        'url_path': 'tersky',
        'id_parsing': 5
    },
    {
        'name': 'Ковдорский',
        'url_path': 'kovdorsky',
        'id_parsing': 6
    },
    {
        'name': 'Кировский',
        'url_path': 'kirovsky',
        'id_parsing': 7
    },
    {
        'name': 'Апатитский',
        'url_path': 'apatity',
        'id_parsing': 8
    },
    {
        'name': 'Мончегорский',
        'url_path': 'monchegorsky',
        'id_parsing': 9
    },
    {
        'name': 'Оленегорский',
        'url_path': 'olenergorsky',
        'id_parsing': 10
    },
    {
        'name': 'Ловозерский',
        'url_path': 'lovozersky',
        'id_parsing': 11
    },
    {
        'name': 'Кольский',
        'url_path': 'kola',
        'id_parsing': 12
    },
    {
        'name': 'Североморский',
        'url_path': 'severomorsky',
        'id_parsing': 13
    },
    {
        'name': 'Александровский',
        'url_path': 'alexandrovsky',
        'id_parsing': 14
    },
    {
        'name': 'Печенгский',
        'url_path': 'pechenga',
        'id_parsing': 15
    }
]
class Command(BaseCommand):
    help = 'add base personal centers in database'

    def handle(self, *args, **options):
        for pc in PCS:
            try:
                result = PC.objects.filter(
                    name=pc['name'],
                    id_parsing=pc['id_parsing'],
                    url_path=pc['url_path']
                )

                if result.count() == 0:
                    pc_new = PC(
                        name=pc['name'],
                        id_parsing=pc['id_parsing'],
                        url_path=pc['url_path']
                    )
                    pc_new.save()

                    self.stdout.write(
                        self.style.SUCCESS('Successfully created personal center "%s"' % pc['name'])
                    )
            except Exception as ex:
                raise CommandError('Problem with personal center "%s" error:  %s' % (pc['name'], ex))