"""
URL configuration for hunterproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from hunterproject import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    #Dynamic URL
    path("aboutus/", views.aboutus, name='aboutus'),
    path("course/", views.course, name='course'),
    # path('course/<int:course_id>', views.course_detail, name='course_detail'), 
    path('course/<slug:course_id>', views.course_detail, name='course_detail'), #Doest not Work with
]