"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PrivacyView.as_view(), name='privacy'),
    path('service/', views.ServiceView.as_view(), name='service'),
]