from django.urls import path
from . import views

app_name = 'todoweb'

urlpatterns = [
    path('', views.index, name='index'),
]