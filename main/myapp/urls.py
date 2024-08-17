"""
URL configuration for foodcourt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   
    path('',views.home,name='HomePage'),
    path('book_table/',views.book_table,name='BookTablePage'),
    path('contact/',views.contact,name='ContactPage'),
    path('about/',views.about,name='AboutPage'),
    path('register/',views.register,name='RegisterPage'),
    path('check_user_exist/',views.check_user_exist,name='check_user_exist'),
    path('login/',views.signin,name='LoginPage'),
    path('dashboard/',views.dashboard,name='DashboardPage'),
    path('logout/',views.user_logout,name='LogoutPage'),
    path('dishes/',views.all_dishes,name='all_dishes'),
    path('team/',views.team,name='TeamPage'),
    
    
    
    path('review/',views.review,name='ReviewPage'),
    path('viewmenu/<category>/',views.viewmenu,name='ViewMenuPage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()
