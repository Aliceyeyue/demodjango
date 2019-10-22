"""django1017 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from Foods.views import *
from django1017.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('shop/',shop),
    path('tr/',tr),
    path('agp/',ajax_get_page),
    path('agd/',ajax_get_data),
    path('p_form/',p_form),
    path('form_check/',form_check),
    path('setcookie/',setCookie),
    path('del_cookie/',del_cookie)
]
urlpatterns += [
    path('add_food_type/', add_food_type),
    path('add_food/', add_food),
    path('add_shop/', add_shop),

]
urlpatterns += [
    path('register/',register),
    path('login/',login),
    path('logout/',logout),
]
urlpatterns += [
    path('foods/',csrf_exempt(FoodView.as_view())),
    path('ajax_vue/',ajax_vue),
    path('meishi/',meishi)
                ]
from Foods.urls import router
urlpatterns += router.urls