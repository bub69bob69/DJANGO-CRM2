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
    path('record/<int:pk>', views.customer_record, name='record_'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record_'),
    path('add_record/', views.add_record, name='add_record_'),
    path('update_record/<int:pk>', views.update_record, name='update_record_'),
    


]
