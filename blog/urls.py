
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import allblogs
from blog.views import detail
urlpatterns = [
    path('',allblogs,name='allblogs'),
    path('<int:blog_id>/',detail,name='detail'),
]
