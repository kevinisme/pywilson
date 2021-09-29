from django.urls import include, path

from twinbird import views

app_name = 'twinbird'

urlpatterns = [
    path('index/', views.index , name= 'index'),
    path('list/', views.list , name= 'list'),
    path('dismiss/<str:pk>', views.dismiss , name= 'dismiss'),

]


