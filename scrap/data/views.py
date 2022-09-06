
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *


# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    """All curd operation are perfrom in this views"""
    queryset = Player.objects.filter()
    serializer_class = PlayerSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """method wise serializers"""
        if self.action in ['update', 'partial_update', 'destroy']:
            return PlayerdetailSerializers
        else:
            return PlayerSerializers


class PositionViewSet(viewsets.ModelViewSet):
    """All curd operation are perfrom in this views"""
    queryset = Position.objects.filter()
    serializer_class = PositionSerializers


class HighSchoolViewSet(viewsets.ModelViewSet):
    """All curd operation are perfrom in this views"""
    queryset = HighSchool.objects.filter()
    serializer_class = HighSchoolSerializers
    permission_classes = [permissions.IsAuthenticated]


class TeamViewSet(viewsets.ModelViewSet):
    """All curd operation are perfrom in this views"""
    queryset = Team.objects.filter()
    serializer_class = TeamSerializers
    permission_classes = [permissions.IsAuthenticated]


class HardcommitViewSet(viewsets.ModelViewSet):
    """All curd operation are perfrom in this views"""
    queryset = TwitterInfo.objects.filter()
    serializer_class = HardcommitSerializers
    permission_classes = [permissions.IsAuthenticated]


class TwitterViewset(viewsets.ModelViewSet):
    queryset = TwitterInfo.objects.filter()
    serializer_class = TwitterSerializers
    permission_classes = [permissions.IsAuthenticated]


class YearViewset(viewsets.ModelViewSet):
    queryset = Year.objects.filter()
    serializer_class = YearSerializers
    permission_classes = [permissions.IsAuthenticated]


class StateViewset(viewsets.ModelViewSet):
    queryset = State.objects.filter()
    serializer_class = StateSerializers
    permission_classes = [permissions.IsAuthenticated]


class CityViewset(viewsets.ModelViewSet):
    queryset = City.objects.filter()
    serializer_class = CitySerializers
    permission_classes = [permissions.IsAuthenticated]


class CountryViewset(viewsets.ModelViewSet):
    queryset = Country.objects.filter()
    serializer_class = CountrySerializers
    permission_classes = [permissions.IsAuthenticated]


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.filter()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        """giving condition to user and superuser"""
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(id=user.id)


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializers(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializers(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
