from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('register/', views.register, name = 'register'),
    path('login/',views.user_login , name='login'),
    path('logout/', views.logout_user , name='logout'),
    path('first_lesson/', views.firstlesson, name = 'first_lesson'),

]
