"""ProTwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from AppTwo import views

app_name = 'AppTwo'  ##for template tagging


urlpatterns = [
    path('base/',views.base, name='base'),
    path('register/',views.register, name='Register'),
    path('user_login/',views.user_login, name='user_login'),
    path('users/',views.users, name='users'),
    path('users_old/',views.users_old, name='users2'),
    path('form_page/',views.form_name_view, name='form_name_view'),

    path('',views.help, name='help'),
]
