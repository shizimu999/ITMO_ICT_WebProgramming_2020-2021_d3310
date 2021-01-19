"""AAA URL Configuration

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
from django.urls import path
from ABC import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bxxxx/<int:poll_id>/', views.detail),
    path('personsdata/',views.person_list.as_view()),
    path('persondata/<int:pk>/',views.person_data.as_view()),
    path('deleteperson/<int:pk>/',views.delete_person_data),
    path('personupdata/<int:pk>/',views.personUpdateView.as_view()),
    path('createperson/',views.create_view)
]
