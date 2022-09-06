from django.db import models

# Create your models here.
from django.db import models


# Create your models here.


class Country(models.Model):
    """country details table"""
    name = models.CharField(max_length=100,null=True)


class State(models.Model):
    """state details table"""
    name = models.CharField(max_length=100,null=True)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)


class City(models.Model):
    """state details table"""
    name = models.CharField(max_length=100,null=True)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)


class Year(models.Model):
    """ year details table"""
    name = models.CharField(max_length=100,null=True)


class Position(models.Model):
    """postion of player details table"""
    position = models.CharField(max_length=100, null=True)


class HighSchool(models.Model):
    """school of player details table"""
    name = models.CharField(max_length=100, null=True)


class Team(models.Model):
    """team of player details table"""
    name = models.CharField(max_length=5000,null=True)
    logo = models.URLField(null=True)


class Offer(models.Model):
    """players offer details table"""
    team= models.ManyToManyField(Team)


class Player(models.Model):
    """players details table"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.URLField()
    height = models.CharField(max_length=2000,null=True)
    weight = models.CharField(max_length=2000,null=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    year_id = models.ForeignKey(Year, on_delete=models.CASCADE)
    school_id = models.ForeignKey(HighSchool, on_delete=models.CASCADE)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE)
    offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE)


class Hardcommit(models.Model):
    """player commit and recruiter details details table"""

    commit = models.CharField(max_length=100)
    recruited_by = models.CharField(max_length=100)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class TwitterInfo(models.Model):
    """players twitter details table"""

    username = models.CharField(max_length=100, null=True)
    follower_count = models.IntegerField(null=True)
    following_count = models.IntegerField(null=True)
    twitter_count = models.IntegerField(null=True)
    retweet_count = models.IntegerField(null=True)
    last_tweet = models.CharField(max_length=253,null=True)
    location = models.CharField(max_length=100, null=True)
    profile_name = models.CharField(max_length=30, null=True)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
