from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from basic_app import views
app_name = "basic_app"

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),

]
