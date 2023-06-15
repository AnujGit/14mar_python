"""
URL configuration for DigitalSociety project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Chairman import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('profile/', views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('addmedia/', views.add_media, name='addmedia'),
    path('imagegallery/', views.image_gallery, name='imagegallery'),
    path('videogallery/', views.video_gallery, name='videogallery'),
    path('deletevideo/<int:pk>', views.deletevideo, name='deletevideo'),
    path('deleteimage/<int:pk>', views.deleteimage, name='deleteimage'),
    path('addmember/', views.addmember, name='addmember'),
    path('allmembers/', views.allmembers, name='allmembers'),
    
]
