from django.urls import path, include
from .views import *

app_name = 'data'
"""for user list"""
Playerapi = PlayerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Profile_list = PlayerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
Positionapi = PlayerViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Highschoolapi = HighSchoolViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Teamapi = TeamViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Hardcommitapi = HardcommitViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Twitterapi = TwitterViewset.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Userstapi = UserViewset.as_view({
    'get': 'list'
})
Usertapi = UserViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Cityapi = CityViewset.as_view({
    'get': 'list'
})
Cityapi2 = CityViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Countryapi = CountryViewset.as_view({
    'get': 'list'
})
Countryapi2 = CountryViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Yearapi = YearViewset.as_view({
    'get': 'list'
})
Yearapi2 = YearViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
urlpatterns = [
    path('', Profile_list, name='playerapi'),
    path('<int:pk>/', Playerapi, name='playerapi2'),
    path('position/', Positionapi, name='positionapi'),
    path('school/', Highschoolapi, name='highschoolapi'),
    path('team/', Teamapi, name='Teamapi'),
    path('commit/', Hardcommitapi, name='Hardcommitapi'),
    path('twitter/', Twitterapi, name='Hardcommitapi'),
    path('user/', Userstapi, name='userapi'),
    path('user/<int:pk>/', Usertapi, name='userapi2'),
    path('register/', RegistrationAPI.as_view(), name="register"),
    path('login/', LoginAPI.as_view(), name='login'),
    path('year/', Yearapi, name='yearapi'),
    path('year/<int:pk>', Yearapi2, name='yearapi2'),
    path('city/', Cityapi, name='cityapi'),
    path('city/<int:pk>', Cityapi2, name='cityapi2'),
    path('country/', Countryapi, name='countryapi'),
    path('country/<int:pk>', Countryapi2, name='countryapi2'),
]
