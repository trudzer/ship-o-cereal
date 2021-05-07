"""ship O'Cereal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from contact_form import views

urlpatterns = [
    path('', include('cereal.urls')),
    path('admin/', admin.site.urls),
    path('cereals/', include('cereal.urls')),
    path('manufacturers/', include('manufacturer.urls')),
    path('user/', include('user.urls')),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('feedback/', views.feedback, name="feedback"),
    path('about_us/',views.about_us, name="about_us")
]
