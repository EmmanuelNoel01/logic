from django.urls import path
from . import views


urlpatterns =[
   path('',views.sender,name='sender'),
  path('index/',views.index,name='index'),
   path('register/', views.register, name='register'),
#   path('login/',views.login,name='login'),
]