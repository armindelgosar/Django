from django.urls import path
from . import views

app_name = "advertiser_management"
urlpatterns = [
    path('', views.index, name='index'),
    path('ads', views.show_message, name='show_message'),
    path('make_ad', views.make_ad, name='create_ad'),
    path('<int:pk>/',
         views.AdRedirectView.as_view()
         , name='ad-redirect'),
]
