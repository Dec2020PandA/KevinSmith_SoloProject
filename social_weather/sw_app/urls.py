from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create', views.create),
    path('vote/<poll_id>/', views.vote),
    path('results/<poll_id>/', views.results),
    path('weather', views.weather),
    path('delete/<poll_id>/', views.delete_poll),
]