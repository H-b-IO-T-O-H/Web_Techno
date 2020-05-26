from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from django.urls import path
from accounts import views
from accounts.models import User

app_name = 'accounts'
urlpatterns = [

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.registration_view, name='registration'),
    path('settings/', views.settings_view, name='settings'),

]