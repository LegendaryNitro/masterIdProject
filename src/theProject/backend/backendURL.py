from django.urls import path
from .views import *


urlpatterns = [

#api register users
path('register-list/', registerList, name="register-list"),
path('register-detail/<str:pk>/', registerDetail, name="register-detail"),
path('register-create/', registerCreate, name="register-create2"),
path('register-update/<str:pk>/', registerUpdate, name="register-update"),
path('register-delete/<str:pk>/', registerDelete, name="register-delete"),

]