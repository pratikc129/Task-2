from django.urls import path, include
from .views import *

app_name = 'players'
"""for user list"""
Playerapi_detail = PlayerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Profile_list = PlayerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
Positionapi_list = PositionViewSet.as_view({
    'get': 'list'
})
Positionapi_detail = PositionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Highschoolapi = HighSchoolViewSet.as_view({
    'get': 'list'
})
Highschoolapi2 = HighSchoolViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Teamapi_list = TeamViewSet.as_view({
    'get': 'list'
})
Teamapi_detail = TeamViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Hardcommitapi_list = HardcommitViewSet.as_view({
    'get': 'list'
})
Hardcommitapi_detail = HardcommitViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Twitterapi_list = TwitterViewset.as_view({
    'get': 'list'
})
Twitterapi_detail = TwitterViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Userstapi_list = UserViewset.as_view({
    'get': 'list'
})
Usertapi_detail = UserViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Cityapi_list = CityViewset.as_view({
    'get': 'list'
})
Cityapi_detail = CityViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Countryapi_list = CountryViewset.as_view({
    'get': 'list'
})
Countryapi_detail = CountryViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Yearapi_list = YearViewset.as_view({
    'get': 'list'
})
Yearapi_detail = YearViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
Stateapi_list = StateViewset.as_view({
    'get': 'list'
})
Stateapi_detail = StateViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
offerapi_list = OfferViewset.as_view({
    'get': 'list'
})
offerapi_detail = OfferViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
urlpatterns = [
    path('', Profile_list, name='playerapi'),
    path('<int:pk>/', Playerapi_detail, name='playerapi2'),
    path('position/', Positionapi_list, name='positionapi'),
    path('position/<int:pk>/', Positionapi_detail, name='positionapi2'),
    path('state/', Stateapi_list, name='stateapi'),
    path('state/<int:pk>/', Stateapi_detail, name='stateapi2'),
    path('school/', Highschoolapi, name='highschoolapi'),
    path('school/<int:pk>/', Highschoolapi2, name='highschoolapi2'),
    path('team/', Teamapi_list, name='Teamapi'),
    path('team/<int:pk>/', Teamapi_detail, name='Teamapi2'),
    path('commit/', Hardcommitapi_list, name='Hardcommitapi'),
    path('commit/<int:pk>/', Hardcommitapi_detail, name='Hardcommitapi2'),
    path('twitter/', Twitterapi_list, name='twitterapi'),
    path('twitter/<int:pk>/', Twitterapi_detail, name='twitterapi2'),
    path('user/', Userstapi_list, name='userapi'),
    path('user/<int:pk>/', Usertapi_detail, name='userapi2'),
    path('register/', RegistrationAPI.as_view(), name="register"),
    path('login/', LoginAPI.as_view(), name='login'),
    path('year/', Yearapi_list, name='yearapi'),
    path('year/<int:pk>', Yearapi_detail, name='yearapi2'),
    path('city/', Cityapi_list, name='cityapi'),
    path('city/<int:pk>', Cityapi_detail, name='cityapi2'),
    path('country/', Countryapi_list, name='countryapi'),
    path('country/<int:pk>', Countryapi_detail, name='countryapi2'),
    path('offer/', offerapi_list, name='offerapi'),
    path('offer/<int:pk>', offerapi_detail, name='offerapi2')

]
