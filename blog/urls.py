from django.urls import path
from . import views

urlpatterns = [
   path('',views.post_list, name = 'post_list'),
   path('homepage',views.homepage, name='Make SA Hall Great Again'),
   path('post/<int:pk>/', views.post_detail, name='post_detail'),
   path('post/new/',views.post_new, name='post_new'),
   path('registration/',views.registration, name='registration'), #registration url
]