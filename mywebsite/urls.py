"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from mywebsite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('login/',views.login),
    path('success1/',views.success1),
    path('signup/',views.signup),
    path('success2/',views.success2),
    path('dashboard/',views.dashboard),
    path('about/',views.about),
    path('event/',views.event),
    path('explore/',views.explore),
    path('resources/',views.resources),
    path('contact/',views.contact),
    path('success/',views.success),
    path('job/',views.job),
    path('job_details/<int:sid>',views.job_page),
    path('donate/',views.donate),
    path('done/',views.done),
    path('apply/',views.apply),
    path('confirm/',views.confirm),
    path('team/',views.team),
    path('team_details/<int:sid>',views.team_page),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

