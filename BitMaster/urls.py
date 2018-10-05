"""BitMaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from main import views as main_views
from django.contrib import admin
from django.urls import path
import user.views as user_view
import service.views as service_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index),

    # user
    path('user/joinform/', user_view.joinform),
    path('user/join', user_view.join),
    path('user/joinsuccess/', user_view.joinsuccess),
    path('user/loginform/', user_view.loginform),
    path('user/login', user_view.login),
    path('user/logout', user_view.logout),


    # service
    path('service/yniScore', service_view.yniScore),
    path('service/yniCompare', service_view.yniCompare),
    path('service/yniAverage', service_view.yniAverage)


]
