from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index') # empty quotes ("") means the home page of our app
]
