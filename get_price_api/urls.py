from django.urls import path,include
from get_price_api import views
from rest_framework.routers import DefaultRouter


urlpatterns=[
    path('get-price/',views.GetPrice.as_view()),

]
