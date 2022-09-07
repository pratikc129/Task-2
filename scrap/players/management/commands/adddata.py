from django.core.management.base import BaseCommand
from ...models import *
import openpyxl
import ast
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


class Command(BaseCommand):
    help = "A commands to add players from an Excel file to the database"

    def handle(self, *args, **options):
        global dic
        workbook = openpyxl.load_workbook("/home/pratikc/PycharmProjects/t-2/scrap/Teaminfo.xlsx")
        sheet = workbook.active
        fieldname = ["Playername", "Image", "Position", "Height", "Weight", "Highschool", "City", "Year",
                     "Logo&name", "Commited", "Commited_College", "Recruited_by", "Twitter"]
        for i in range(1, sheet.max_row + 1):
            l2 = []
            for cell in sheet[i + 1]:
                l2.append(cell.value)
            dic = dict(zip(fieldname, l2))
            player = dic.get("Playername")
            value = player.split(' ')
            ml = (value[0])
            print("first name", ml)
            cl = (value[1])
            a = dic.get("Highschool")
            print(a)
            print(ml)
            print(cl)
            try:
                sd = Player.objects.get(first_name=ml, last_name=cl, image=dic.get("Image"), height=dic.get("Height"), )
            except ObjectDoesNotExist:
                pos = dic.get("Position")
                positiondata = Position.objects.get_or_create(position=pos)
                year = dic.get("Year")
                ert = Year.objects.get_or_create(name=year)
                ft = dic.get("Logo&name")
                yut = ast.literal_eval(ft)
                team_logo = yut.keys()
                team_name = yut.values()
                for i, j in yut.items():
                    try:
                        l = Team.objects.get(name=j)
                        print()
                    except ObjectDoesNotExist:
                        teamdata = Team.objects.get_or_create(name=j, logo=i)
                cities = dic.get("City")
                country = Country.objects.get_or_create(name="USA")
                country_id = Country.objects.get(name="USA")
                value = cities.split(', ')
                state = (value[1])
                city = (value[0])
                statename = State.objects.get_or_create(name=state, country_id=country_id)
                state_id = State.objects.get(name=state)
                cityname = City.objects.get_or_create(name=city, state_id=state_id)
                school = dic.get("Highschool")
                highschool = HighSchool.objects.get_or_create(name=school)
                print(highschool)
                tyu = dic.get("Logo&name")
                team = ast.literal_eval(tyu)
                te = Offer.objects.create()
                for logo, name in team.items():
                    teamid = Team.objects.filter(name=name, logo=logo)
                    te.team.add(*teamid)
                offers_id = te.id
                weight = dic.get("Weight")
                height = dic.get("Height")
                image = dic.get("Image")

                city_id = City.objects.get(name=city, state_id=state_id)
                year_id = Year.objects.get(name=year)
                school_id = HighSchool.objects.get(name=school)
                position_id = Position.objects.get(position=pos)
                offers = Offer.objects.get(pk=offers_id)
                Playerdata = Player.objects.get_or_create(first_name=ml, last_name=cl, image=image, height=height,
                                                          weight=weight, city_id=city_id, year_id=year_id,
                                                          school_id=school_id, position_id=position_id, offer_id=offers)

                commit = dic.get("Commited")
                recruit = dic.get("Recruited_by")
                commitedclg = dic.get("Commited_College")
                playerid = Player.objects.get(first_name=ml, last_name=cl, image=image, position_id=position_id)
                if commit == " ":
                    print(" ")
                else:
                    a = Team.objects.get(name=commitedclg)
                    hardcommit = Hardcommit.objects.create(commit=commit, recruited_by=recruit, player=playerid, team=a)

                try:
                    twitter_profile = dic.get("Twitter")
                    twiter = TwitterInfo.objects.get_or_create(username=twitter_profile, player_id=playerid)
                except MultipleObjectsReturned:
                    pass
