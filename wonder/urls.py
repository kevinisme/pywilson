from django.urls import include, path

from wonder import views

app_name = 'wonder'

urlpatterns = [
    path('index/', views.index , name= 'index'),
    path('new/', views.new , name= 'new'),
    path('edit/<str:pk>', views.edit , name= 'edit'),
    path('delete/<str:pk>', views.delete , name= 'delete'),

]


