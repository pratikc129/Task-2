from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import *


class SetupTest(APITestCase):
    """setup for all api test cases"""

    def setUp(self):
        self.user = User.objects.create_user(username='pratik', email='sphoeni@gamil.com', password='pass@234',
                                             first_name='pratik', last_name='chakane')
        self.client.login(username="pratik", password="pass@234")
        self.year = Year.objects.create(name='2023')
        self.position = Position.objects.create(position="CB")
        self.highschool = HighSchool.objects.create(name='stv')
        self.country = Country.objects.create(name="India")
        self.state = State.objects.create(name='Maharashtra', country_id=self.country)
        self.city = City.objects.create(name='Pune', state_id=self.state)
        self.team = Team.objects.create(name="Alabama",
                                        logo="https://s3media.247sports.com/Uploads/Assets/288/31/11031288.jpeg?fit=crop&width=100&fit=crop")
        self.offer = Offer.objects.create()
        teamid = Team.objects.get(name='Alabama')
        a = self.offer.team.add(teamid)

        self.player = Player.objects.create(first_name='virat', last_name='kholi',
                                            image='"https://s3media.247sports.com/Uploads/Assets/288/31/11031288.jpeg?fit=crop&width=100&fit=crop"',
                                            height='6-7',
                                            weight='243', city_id=self.city, year_id=self.year,
                                            school_id=self.highschool, position_id=self.position, offer_id=self.offer)
        self.twitter = TwitterInfo.objects.create(id=1, follower_count=2099,
                                                  following_count=2091,
                                                  twitter_count=234, retweet_count=34,
                                                  location='india', last_tweet='hi welcome', player_id=self.player)
        self.user = User.objects.create(id=6, username='ram23', email='ram@gmail.com', first_name='ram',
                                        last_name='kate')
        self.hardcommit = Hardcommit.objects.create(commit='commit', recruited_by='pratik', player=self.player,
                                                    team=self.team)


class YearTest(SetupTest):
    """Year api test cases"""

    def test_year_read(self):
        year = Year.objects.get(name='2023')
        response = self.client.get(reverse('players:yearapi2', args=[year.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_year_delete(self):
        year = Year.objects.get(name='2023')
        response = self.client.delete(reverse('players:yearapi2', args=[year.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_year_update(self):
        update_data = {"name": "2022"}
        year = Year.objects.get(name='2023')
        response = self.client.patch(reverse('players:yearapi2', args=[year.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PositionTest(SetupTest):
    """Position api test cases"""

    def test_position_read(self):
        pos = Position.objects.get(position='CB')
        response = self.client.get(reverse('players:positionapi2', args=[pos.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_position_delete(self):
        pos = Position.objects.get(position='CB')
        response = self.client.delete(reverse('players:positionapi2', args=[pos.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_position_update(self):
        update_data = {"position": "AS"}
        pos = Position.objects.get(position='CB')
        response = self.client.patch(reverse('players:positionapi2', args=[pos.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class HighschoolTest(SetupTest):
    """Highschool api test cases"""

    def test_highschool_read(self):
        school = HighSchool.objects.get(name='stv')
        response = self.client.get(reverse('players:highschoolapi2', args=[school.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_highschool_delete(self):
        school = HighSchool.objects.get(name='stv')
        response = self.client.delete(reverse('players:highschoolapi2', args=[school.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_highschool_update(self):
        update_data = {"name": "sjv"}
        school = HighSchool.objects.get(name='stv')
        response = self.client.patch(reverse('players:highschoolapi2', args=[school.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CountryTest(SetupTest):
    """Country api test cases"""

    def test_country_read(self):
        country = Country.objects.get(name='India')
        response = self.client.get(reverse('players:countryapi2', args=[country.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_delete(self):
        country = Country.objects.get(name='India')
        response = self.client.delete(reverse('players:countryapi2', args=[country.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_country_update(self):
        update_data = {"name": "Uk"}
        country = Country.objects.get(name='India')
        response = self.client.patch(reverse('players:countryapi2', args=[country.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class StateTest(SetupTest):
    """State api test cases"""

    def test_state_read(self):
        state = State.objects.get(name='Maharashtra')
        response = self.client.get(reverse('players:stateapi2', args=[state.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_state_delete(self):
        state = State.objects.get(name='Maharashtra')
        response = self.client.delete(reverse('players:stateapi2', args=[state.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_state_update(self):
        update_data = {"name": "UP"}
        state = State.objects.get(name='Maharashtra')
        response = self.client.patch(reverse('players:stateapi2', args=[state.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CityTest(SetupTest):
    """City api test cases"""

    def test_city_read(self):
        city = City.objects.get(name='Pune')
        response = self.client.get(reverse('players:cityapi2', args=[city.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_city_delete(self):
        city = City.objects.get(name='Pune')
        response = self.client.delete(reverse('players:cityapi2', args=[city.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_city_update(self):
        update_data = {"name": "Negar"}
        city = City.objects.get(name='Pune')
        response = self.client.patch(reverse('players:cityapi2', args=[city.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamTest(SetupTest):
    """Team api test cases"""

    def test_team_read(self):
        team = Team.objects.get(name='Alabama')
        response = self.client.get(reverse('players:Teamapi2', args=[team.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_team_delete(self):
        team = Team.objects.get(name='Alabama')
        response = self.client.delete(reverse('players:Teamapi2', args=[team.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_team_update(self):
        update_data = {"name": "Folrida"}
        team = Team.objects.get(name='Alabama')
        response = self.client.patch(reverse('players:Teamapi2', args=[team.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PlayerTest(SetupTest):
    """Player api test cases"""

    def test_player_read(self):
        player = Player.objects.get(first_name='virat', last_name='kholi', weight='243')
        response = self.client.get(reverse('players:playerapi2', args=[player.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_player_delete(self):
        player = Player.objects.get(first_name='virat', last_name='kholi', weight='243')
        response = self.client.delete(reverse('players:playerapi2', args=[player.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_player_update(self):
        update_data = {"weight": "345"}
        player = Player.objects.get(first_name='virat', last_name='kholi', weight='243')
        response = self.client.patch(reverse('players:playerapi2', args=[player.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TwitterTest(SetupTest):
    """Twitter api test cases"""

    def test_twitter_read(self):
        twitter = TwitterInfo.objects.get(id=1)
        response = self.client.get(reverse('players:twitterapi2', args=[twitter.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_twitter_delete(self):
        twitter = TwitterInfo.objects.get(id=1)
        response = self.client.delete(reverse('players:twitterapi2', args=[twitter.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_twitter_update(self):
        update_data = {"weight": "345"}
        twitter = TwitterInfo.objects.get(id=1)
        response = self.client.patch(reverse('players:twitterapi2', args=[twitter.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserTest(SetupTest):
    """User api test cases"""

    def test_user_read(self):
        user = User.objects.get(first_name='ram', last_name='kate')
        response = self.client.get(reverse('players:userapi2', args=[user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete(self):
        user = User.objects.get(first_name='ram', last_name='kate')
        response = self.client.delete(reverse('players:userapi2', args=[user.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_update(self):
        update_data = {"username": "raju12"}
        user = User.objects.get(first_name='ram', last_name='kate')
        response = self.client.patch(reverse('players:userapi2', args=[user.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class HardcommitTest(SetupTest):
    """Hardcommit api test cases"""

    def test_user_read(self):
        commmit = Hardcommit.objects.get(commit='commit', recruited_by='pratik')
        response = self.client.get(reverse('players:Hardcommitapi2', args=[commmit.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete(self):
        commmit = Hardcommit.objects.get(commit='commit', recruited_by='pratik')
        response = self.client.delete(reverse('players:Hardcommitapi2', args=[commmit.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_update(self):
        update_data = {"recruited_by": "lokesh"}
        commmit = Hardcommit.objects.get(commit='commit', recruited_by='pratik')
        response = self.client.patch(reverse('players:Hardcommitapi2', args=[commmit.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OfferTest(SetupTest):
    def test_user_read(self):
        offer = Offer.objects.get()
        response = self.client.get(reverse('players:offerapi2', args=[offer.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_offer_delete(self):
        offer = Offer.objects.get()
        response = self.client.delete(reverse('players:offerapi2', args=[offer.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




