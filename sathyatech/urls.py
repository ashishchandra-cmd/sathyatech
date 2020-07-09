"""sathyatech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.admin_login,name='admin_login_view'),
    path('admin_logout/', views.admin_logout, name='admin_logout_views'),
    path('admin_welcome/', views.admin_welcome,name='admin_welcome_views'),
    path('view_all_scheduled/',views.view_all_scheduled,name='view_all_scheduled_show'),
    path('insert/',views.insert_new_curese_info,name='insert_new_curese_show'),
    path('delete/<int:id>/',views.delete_curese,name='delete_curese_show'),
    path('update/<int:id>/',views.update_course,name='update_course_show')


]
