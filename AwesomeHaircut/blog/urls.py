from django.urls import path
from django.contrib import admin

from . import views

#Blog index
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('<str:post_title>', views.blog_post, name='title'),
]

