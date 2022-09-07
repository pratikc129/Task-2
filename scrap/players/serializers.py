from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class PlayerSerializers(serializers.ModelSerializer):
    """serializer for Player view"""

    class Meta:
        depth = 4
        model = Player
        fields = [
            'first_name', 'last_name', 'image', 'height', 'weight', 'city_id', 'year_id', 'school_id', 'position_id'
        ]


class PlayerdetailSerializers(serializers.ModelSerializer):
    """serializer for Player detail view"""

    class Meta:
        model = Player
        fields = [
            'first_name', 'last_name', 'image', 'height', 'weight'
        ]


class PositionSerializers(serializers.ModelSerializer):
    """serializer for Position view"""

    class Meta:
        model = Position
        fields = [
            'position'
        ]


class HighSchoolSerializers(serializers.ModelSerializer):
    """serializer for HighSchool view"""

    class Meta:
        depth = 3
        model = HighSchool
        fields = [
            'name'
        ]


class TeamSerializers(serializers.ModelSerializer):
    """serializer for Team view"""

    class Meta:
        model = Team
        fields = [
            'name'
        ]


class HardcommitSerializers(serializers.ModelSerializer):
    """serializer for Hardcommit view"""

    class Meta:
        model = Hardcommit
        fields = [
            'commit', 'recruited_by', 'player', 'team'
        ]


class TwitterSerializers(serializers.ModelSerializer):
    """serializer for Player view"""

    class Meta:
        model = TwitterInfo
        fields = [
            'id','username', 'follower_count', 'following_count', 'twitter_count',
            'retweet_count', 'last_tweet',
            'location', 'profile_name', 'player_id'
        ]


class UserSerializers(serializers.ModelSerializer):
    """serializer for User view"""

    class Meta:
        model = User
        fields = 'id', 'username', 'email', 'first_name', 'last_name'


class CreateUserSerializer(serializers.ModelSerializer):
    """serializer for register view"""

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")


class CitySerializers(serializers.ModelSerializer):
    """serializer for city view"""

    class Meta:
        model = City
        fields = 'name', 'state_id'


class StateSerializers(serializers.ModelSerializer):
    """serializer for state view"""

    class Meta:
        model = State
        fields = 'name', 'country_id'


class CountrySerializers(serializers.ModelSerializer):
    """serializer for country view"""

    class Meta:
        model = Country
        fields = '__all__'


class YearSerializers(serializers.ModelSerializer):
    """serializer for year view"""

    class Meta:
        model = Year
        fields = '__all__'

class StateSerializers(serializers.ModelSerializer):
    """serializer for year view"""

    class Meta:
        model = State
        fields = '__all__'

class OfferSerializers(serializers.ModelSerializer):
    """serializer for offer view"""

    class Meta:
        model = Offer
        fields = '__all__'
