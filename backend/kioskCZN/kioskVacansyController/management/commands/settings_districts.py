from django.core.management.base import BaseCommand, CommandError

from kioskVacansyController.models import Districts


DISTRICTS = [
    {
        "id":0,
        "name":'Мурманск',
        "min_code":51000001000000000,
        "max_code":51000001999999999,
        "work_places":0,
    },
    {
        "id":1,
        "name":'Видяево',
        "min_code":51000000004000000,
        "max_code":51000000004999999,
        "work_places":0
    },
    {
        "id":2,
        "name":'Апатиты',
        "min_code":51000002000000000,
        "max_code":51000002999999999,
        "work_places":0,
    },
    {
        "id":3,
        "name":'Заозерск',
        "min_code":51000003000000000,
        "max_code":51000003999999999,
        "work_places":0
    },
    {
        "id":4,
        "name":'Кировск',
        "min_code":51000005000000000,
        "max_code":51000005999999999,
        "work_places":0
    },
    {
        "id":5,
        "name":'Мончегорск',
        "min_code":51000006000000000,
        "max_code":51000006999999999,
        "work_places":0
    },
    {
        "id":6,
        "name":'Оленегорск',
        "min_code":51000007000000000,
        "max_code":51000007999999999,
        "work_places":0
    },
    {
        "id":7,
        "name":'Островной',
        "min_code":51000008000000000,
        "max_code":51000008999999999,
        "work_places":0
    },
    {
        "id":8,
        "name":'Полярные Зори',
        "min_code":51000009000000000,
        "max_code":51000009999999999,
        "work_places":0
    },
    {
        "id":9,
        "name":'Полярный',
        "min_code":51000010000000000,
        "max_code":51000019999999999,
        "work_places":0
    },
    {
        "id":10,
        "name":'Североморск',
        "min_code":51000011000000000,
        "max_code":51000011999999999,
        "work_places":0
    },
    {
        "id":11,
        "name":'Гаджиево',
        "min_code":51000012000000000,
        "max_code":51000012999999999,
        "work_places":0
    },
    {
        "id":12,
        "name":'Снежногорск',
        "min_code":51000013000000100,
        "max_code":51000013999999999,
        "work_places":0
    },
    {
        "id":13,
        "name":'Оленегорск-2',
        "min_code":51000016000000000,
        "max_code":51000016999999999,
        "work_places":0
    },
    {
        "id":14,
        "name":'Кандалакшский район',
        "min_code":51001000000000000,
        "max_code":51001999999999999,
        "work_places":0
    },
    {
        "id":15,
        "name":'Ковдорский район',
        "min_code":51002000000000000,
        "max_code":51002999999999999,
        "work_places":0
    },
    {
        "id":16,
        "name":'Кольский район',
        "min_code":51003000000000000,
        "max_code":51003999999999999,
        "work_places":0
    },
    {
        "id":17,
        "name":'Ловозерский район',
        "min_code":51004000000000000,
        "max_code":51004999999999999,
        "work_places":0
    },
    {
        "id":18,
        "name":'Печенгский район',
        "min_code":51005000000000000,
        "max_code":51005999999999999,
        "work_places":0
    },
    {
        "id":19,
        "name":'Терский район',
        "min_code":51006000000000000,
        "max_code":51006999999999999,
        "work_places":0
    }
]


class Command(BaseCommand):
    help = 'add base Districts in database'


    def handle(self, *args, **options):
        for d in DISTRICTS:
            try:
                result = Districts.objects.filter(
                    id=d['id'],
                )

                if result.count() == 0:
                    d_new = Districts(
                        id=d['id'],
                        name=d['name'],
                        min_code=d['min_code'],
                        max_code=d['max_code'],
                        work_places=d['work_places']
                    )
                    d_new.save()

                    self.stdout.write(
                        self.style.SUCCESS('Successfully created district "%s"' % d['name'])
                    )
            except Exception as ex:
                raise CommandError('Problem with district "%s" error:  %s' % (d['name'], ex))