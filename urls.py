from django.contrib import admin
from django.urls import path,include
from send.views import sendmail

urlpatterns = [
  path('',sendmail,name="sendmail")
   ]