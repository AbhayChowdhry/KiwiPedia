from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name ='home'),
    path('programming', views.programming),
    path('fortnite', views.fortnite),
    path('physics', views.physics),
    path('harrypotter', views.haryypotter),
    path('crypto', views.crypto),
    path('cat', views.cat)
]   
