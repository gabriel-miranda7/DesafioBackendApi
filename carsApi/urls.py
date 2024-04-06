"""
URL configuration for carsApi project.

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
from django.contrib import admin #Faz os imports necessários
from django.urls import path 
from carsApi import views 
 
urlpatterns = [ #Configura os caminhos (paths)
    path('admin/', admin.site.urls),
    path('cars/', views.car_List),
    path('cars', views.car_List),
    path('cars/<int:id>', views.car_Detail)
]
