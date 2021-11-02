from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('register/',register, name='register'),
    path('home/',loginPage, name='home'),
    path('profile/',profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name=f'{ff}/login.html'), name='login'),


  
    # path('page/',pageTester, name='page'),
    # path('basetemplate/',baseTemplate, name='baseTemplate'),
    # path('template1/',template1, name='Template1'),
    # path('template2/',template2, name='template2'),
    # path('template3/',template3, name='template3'),
    # template3,
]