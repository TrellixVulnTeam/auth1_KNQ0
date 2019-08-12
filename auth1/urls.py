"""auth1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from app_auth.views import start, register,profile1, profile, AddDevice, ChartData, charts, BarChart, Doughnut, track, map
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',start,name='index' ),
    path('profile/',profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logged_out.html'),name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('AddDevice/', AddDevice, name='AddDevice'),
    path('profile1/', profile1, name='profile1'),
    path('map/', map, name='map'),
    path('chart/', charts.as_view(), name='chart'),
    path('sample/', ChartData.as_view()),
    path('sample1/', BarChart.as_view()),
    path('sample2/', Doughnut.as_view()),
    path('track/', track.as_view()),

]

if settings.DEBUG:
    urlpatterns = urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)