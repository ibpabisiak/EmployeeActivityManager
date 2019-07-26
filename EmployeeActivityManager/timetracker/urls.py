from django.urls import path
from timetracker import views

app_name = 'timetracker'

urlpatterns = [
    path('', views.index, name='index'),
]