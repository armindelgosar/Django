from django.urls import path
from rest_framework.authtoken import views

from .views import *

app_name = "advertiser_management"
urlpatterns = [
    path('', AdvertiserManagement.as_view(), name='advertiser_management'),
    path('ads', ShowAds.as_view(), name='show_ads'),
    path('create_ad', AdCreate.as_view(), name='create_ad'),
    path('ad_detail', AdDetailedList.as_view({'get': 'list'}), name='ad_detail'),
    path('ads2', AdList.as_view(), name='create_ad'),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),

    path('<int:pk>/',
         AdRedirectView.as_view()
         , name='ad-redirect'),
]
