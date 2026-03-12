"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from contact.views import contact_view, subscribe_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('contact/', contact_view, name='contact_page'),
    path('subscribe/', subscribe_view, name='subscribe'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # The main dashboard page
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Actions for managing data
    path('delete-message/<int:id>/', views.delete_message, name='delete_message'),
    path('delete-subscriber/<int:id>/', views.delete_subscriber, name='delete_subscriber'),
]
