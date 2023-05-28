#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('websiteapp2.urls')),
    path('', views.home, name='home_'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout_'),
    path('register/', views.register_user, name='register_'),


]
