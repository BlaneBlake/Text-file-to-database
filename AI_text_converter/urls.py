"""coderslab URL Configuration

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
from django.urls import path
from .views import (DataUploadFormView, ConvertView, ChartsView,
                    PDFGeneratorView, AddUserView, UserListView,
                    LoginView, LogoutView, HomePageView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('data-upload-form/', DataUploadFormView.as_view(), name='upload-form'),
    path('convert-data', ConvertView.as_view(), name='convert-data'),
    path('charts/', ChartsView.as_view(), name='charts'),
    path('pdf/', PDFGeneratorView.as_view(), name='pdf'),
    path('add_user/', AddUserView.as_view(), name='add_user'),
    path('list_users/', UserListView.as_view(), name='list_users'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]