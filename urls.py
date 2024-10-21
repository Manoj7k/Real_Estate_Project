from django.contrib import admin
from django.urls import path
from bulklands import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.agent_registration, name='agent_register'),
    path('inquiry/', views.inquiry, name='inquiry'),
]
