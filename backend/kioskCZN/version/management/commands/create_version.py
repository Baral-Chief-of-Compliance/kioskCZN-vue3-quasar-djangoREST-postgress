from django.core.management.base import BaseCommand, CommandError

from version.models import Version


class Command(BaseCommand):
    help = 'create version of project'

    def handle(self, *args, **options):
        try:
            if (Version.objects.count() == 0):
                Version.objects.create()
                self.stdout.write(
                    self.style.SUCCESS('Successfully create version of project')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS('Version already created')
                )
        except Exception as e:
            raise CommandError('Problem with version manage: %s', e)

            