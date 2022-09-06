from django.core.management.base import BaseCommand
from ...models import *
import openpyxl
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import ast
from selenium.webdriver.common.by import By
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    help = "A commands to add data from an Excel file to the database"

    def handle(self, *args, **options):
        player = Player.objects.all()
        val = player.values('first_name', 'last_name', 'image', 'height',
                            'weight', 'year_id',
                            'school_id', 'position_id', 'city_id', 'offer_id')
        # print(val)
        for i in val.values('first_name', 'last_name', 'image', 'height',
                            'weight', 'year_id',
                            'school_id', 'position_id', 'city_id', 'offer_id'):
            dic = i
            firstname = dic.get("first_name")
            lastname = dic.get("last_name")
            image = dic.get("image")
            height = dic.get("height")
            weight = dic.get("weight")
            year_id = dic.get("year_id")
            school_id = dic.get("school_id")
            city_id = dic.get("city_id")
            position_id = dic.get("position_id")
            offer_id = dic.get("offer_id")
            print(firstname, lastname, image, height, weight, year_id, school_id, city_id, position_id, offer_id)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get("https://247sports.com/Season/2023-Football/Recruits/")
            time.sleep(8)
            search = driver.find_element(By.XPATH,
                                         "/html/body/section[1]/section/div/section["
                                         "2]/section/section/section/div/section[1]/form/input")

            search.send_keys(firstname, " ", lastname)
            time.sleep(4)
            serachit = driver.find_element(By.XPATH,
                                           "/html/body/section[1]/section/div/section["
                                           "2]/section/section/section/div/section[1]/form/button").click()
            time.sleep(4)
            playerlist = driver.find_element(By.XPATH, '//li[@class="name"]/a')
            playerlist.click()
            """scraping position"""
            pos = driver.find_element(By.XPATH,
                                      "/html/body/section[1]/section/div/section/header/div[1]/ul[1]/li[1]/span[2]").text
            print(pos)
            """Updating position"""
            positions = Position.objects.get(id=position_id)
            updated_position = positions.position
            print(updated_position)
            if pos == updated_position:
                print()
            else:
                Position.objects.update(position=updated_position)

            """scraping height"""

            height1 = driver.find_element(By.XPATH,
                                          "/html/body/section[1]/section/div/section/header/div[1]/ul[1]/li[2]/span[2]").text
            print(height1)
            """Updating height"""
            if height1 == height:
                print()
            else:
                Player.objects.update(height=height1)
            """scraping weight"""
            weight1 = driver.find_element(By.XPATH,
                                          "/html/body/section[1]/section/div/section/header/div[1]/ul[1]/li[3]/span[2]").text
            print(weight1)
            """Updating weight"""
            if weight1 == weight:
                print()
            else:
                Player.objects.update(weight=weight1)

            """scraping highschool"""
            try:
                highschool = driver.find_element(By.XPATH,
                                                 "/html/body/section[1]/section/div/section/header/div[1]/ul[3]/li[1]/span[2]").text
                print(highschool)
                highschool1 = HighSchool.objects.get(id=school_id)
                updated_school = highschool1.name
                print(updated_school)
                """Updating highschool"""
                if highschool1 == updated_school:
                    print()
                else:
                    HighSchool.objects.update(name=updated_school)

            except NoSuchElementException:
                pass
            """scraping city"""
            city = driver.find_element(By.XPATH,
                                       "/html/body/section[1]/section/div/section/header/div[1]/ul[3]/li[2]/span[2]").text
            value = city.split(', ')
            state = (value[1])
            city = (value[0])
            print(city)
            city1 = City.objects.get(id=city_id)
            updated_city = city1.name
            print(updated_city)
            """Updating city"""
            if city == updated_city:
                print()
            else:
                City.objects.update_or_create(name=updated_city)

            """scraping year"""
            year = driver.find_element(By.XPATH,
                                       "/html/body/section[1]/section/div/section/header/div[1]/ul[3]/li[3]/span[2]").text
            print(year)
            year1 = Year.objects.get(id=year_id)
            updated_year = year1.name
            print(updated_year)

            """Updating year"""

            if year == updated_year:
                print()
            else:
                Year.objects.update(name=updated_year)

            """scraping image data"""
            image_link = driver.find_element(By.XPATH, "//img[@class='jsonly']").get_attribute("src")
            print("image link", image_link)
            """updating imge data"""
            if image_link == image:
                print()
            else:
                Player.objects.update_or_create(image=image_link)


            # commited = driver.find_element(By.XPATH,
            #                                '//span[@class="college-comp__interest-level '
            #                                'college-comp__interest-level--committed-bg"]').text
            commited = driver.find_element(By.XPATH,"/html/body/section[1]/section/div/section/section/div/ul/li[1]/span").text
            print(commited)
            recruited_by = driver.find_elements(By.XPATH,
                                                "/html/body/section[1]/section/div/section/section/div/ul/li["
                                                "1]/div[3]")
            for s in recruited_by:
                t = s.text
            print(t)
            commitedclg = driver.find_element(By.XPATH,
                                              "/html/body/section[1]/section/div/section/section/div/ul/li["
                                              "1]/div[1]/a[1]").text
            print(commitedclg)

            id1=Player.objects.get(first_name=firstname,last_name=lastname,height=height1,weight=weight1)
            te=id1.id
            a=Team.objects.get(name=commitedclg)
            d=Hardcommit.objects.filter(player=te).update(commit=commited,recruited_by=t,team=a)






















            # driver.switch_to.frame('twitter-widget-0')
            # time.sleep(4)
            # twitters = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/a/div/a/span").text
            # value = twitters.split('@')
            # twittername = ("@" + value[1])
            # print("Account_Name", twittername)
            # break




        # for i in range(1,3):
        #     player_info=Player.objects.get(id=i)
        #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #     driver.maximize_window()
        #     driver.get("https://247sports.com/Season/2023-Football/Recruits/")
        #     time.sleep(8)
        #
        #     search = driver.find_element(By.XPATH,
        #                                  "/html/body/section[1]/section/div/section["
        #                                  "2]/section/section/section/div/section[1]/form/input")
        #
        #     search.send_keys(player_info.first_name," ",player_info.last_name)
        #     time.sleep(4)
        #     serachit = driver.find_element(By.XPATH,
        #                                    "/html/body/section[1]/section/div/section["
        #                                    "2]/section/section/section/div/section[1]/form/button").click()
        #
        #     time.sleep(4)
        #     playerlist = driver.find_element(By.XPATH, '//li[@class="name"]/a')
        #     playerlist.click()
        #     """scraping position"""
        #     pos = driver.find_element(By.XPATH,
        #                               "/html/body/section[1]/section/div/section/header/div[1]/ul[1]/li[1]/span[2]").text
        #     print(pos)
        #     """Updating position"""
        #     positions = Position.objects.filter(id=i).update(pos=)
        #     updated_position = positions.position
        #     print(updated_position)
        #     if pos == updated_position:
        #         print()
        #     else:
        #         Position.objects.update(position=updated_position)

