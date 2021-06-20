from django.urls import path
from . import views

urlpatterns = [
   path('',views.post_list, name = 'post_list'),
   path('homepage',views.Index.html, name='Make SA Hall Great Again'),
]