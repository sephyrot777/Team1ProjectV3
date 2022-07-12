"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsView.as_view(), name='news'),
    path('announce/', views.AnnounceView.as_view(), name='announce'),
    path('teamplayer/', views.TeamPlayerView.as_view(), name='teamPlayer'),
]