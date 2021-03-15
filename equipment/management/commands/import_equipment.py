import os
import json
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

from equipment.models import Equipment


class Command(BaseCommand):
    help = 'Import equipment from old engine into models'
    option_list = BaseCommand.option_list + (
        make_option(
            "-f",
            "--file",
            dest="filename",
            help="specify import file",
            metavar="FILE"
        ),
    )

    def handle(self, *args, **options):
        # make sure file option is present
        if options['filename'] is None:
            raise CommandError("Option `--file=...` must be specified.")

        # make sure file path resolves
        if not os.path.isfile(options['filename']):
            raise CommandError("File does not exist at the specified path.")
        # load json
        with open(options['filename']) as json_file:
            eq = json.load(json_file)
        for item in eq:
            if item['owner'] != 0:
                continue
            new_item = {
                'name': item['name'],
                'speed': item['szyb'],
                'repair': item['repair'],
                'cost': item['cost'],
                'dexterity': item['zr'],
                'endurance': item['wt'],
                'max_endurance': item['maxwt'],
                'shop': True,
                'power': item['power'],
                'status': item['status'],
                'magic': True if item['magic'] == 'Y' else False,
                'two_handed': True if item['twohand'] == 'Y' else False,
                'poison': item['poison'],
                'eq_type': item['type'],
                'level': item['minlev']
            }
            Equipment.objects.get_or_create(**new_item)
