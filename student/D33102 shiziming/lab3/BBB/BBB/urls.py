"""BBB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from racer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grouplist/',views.group_list),
    path('groupdeta/<int:pk>/',views.group_deta.as_view()),
    path('creategroup/',views.create_group),
    path('createracer/',views.create_racer),
    path('updetaracer/<int:pk>/',views.racerUpdateView.as_view()),
    path('deleracer/<int:pk>/',views.delete_racer),
    path('accounts/', include('allauth.urls')),
    path('No1/<int:pk>/', views.car_type.as_view()),
    path('up/<int:pk>/', views.AuthorCreate2.as_view()),
    path('create/', views.AuthorCreate.as_view()),
    path('delete_result/<int:pk>/', views.delete_result),
    path('result_list/', views.result_list),
]
