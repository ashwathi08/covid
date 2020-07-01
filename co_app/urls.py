from django.urls import path
from co_app import views

urlpatterns=[
    path('',views.HomePageView),
]