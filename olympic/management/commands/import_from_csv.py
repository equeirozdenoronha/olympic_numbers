import os

from django.core.management.base import BaseCommand

from olympic.models import NOC, Athlete

print(os.getcwd())


class Command(BaseCommand):
    def import_noc_from_csv_file_noc(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        lines = os.path.join(dir_path, "noc_regions.csv")
        fh = open(lines)
        for line in fh.readlines():
            noc_data = line.split(",")
            try:
                noc, created = NOC.objects.get_or_create(
                    noc=noc_data[0],
                    country_name=noc_data[1],
                    notes=noc_data[2]
                )
                if created:
                    noc.save()
                    print("\nNOC, {}, has been saved.".format(noc))
            except Exception as ex:
                print(str(ex))

    def import_noc_from_csv_file_athlete(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        lines = os.path.join(dir_path, "athlete_events.csv")
        fh = open(lines)
        print()
        for line in fh.readlines():
            athlete_data = line.split(',')
            try:
                athlete, created = Athlete.objects.get_or_create(
                    athlete_id=int(athlete_data[0].strip('\"')),
                    name=athlete_data[1].strip('\"'),
                    sex=athlete_data[2].strip('\"'),
                    age=athlete_data[3].strip('\"'),
                    height=athlete_data[4].strip('\"'),
                    weight=athlete_data[5].strip('\"'),
                    team=athlete_data[6].strip('\"'),
                    noc=NOC.objects.get(noc=athlete_data[7].strip('\"')),
                    games=athlete_data[8].strip('\"'),
                    year=athlete_data[9].strip('\"'),
                    season=athlete_data[10].strip('\"'),
                    city=athlete_data[11].strip('\"'),
                    sport=athlete_data[12].strip('\"'),
                    event=athlete_data[13].strip('\"'),
                    medal=athlete_data[14].strip('\"')
                )
                if created:
                    athlete.save()
                    print("\nAthlete, {}, has been saved.".format(athlete.name))
            except Exception as ex:
                print(str(ex))

    def handle(self, *args, **options):
        """
        Call the function to import data
        """
        self.import_noc_from_csv_file_noc()
        # self.import_noc_from_csv_file_athlete()
