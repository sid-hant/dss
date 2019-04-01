"""dss URL Configuration

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
from django.urls import path
from team.views import showTeams
from django.conf.urls.static import static
from django.conf import settings
from player.views import showPlayers, playerDetail, playerSearch



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', showTeams, name="home" ),
    path('team/<pk>', showPlayers, name="player_list"),
    path('player/<pk>', playerDetail, name="player_detail"),
    path('replace-player/<pk>', playerSearch, name="player_search")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
