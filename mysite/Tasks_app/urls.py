
from django.urls import path

from . import views 

urlpatterns = [
  
    path('', views.home),
    path('task/<id_task>', views.task),
    path('add_task/', views.add_task),
    path('edit_task/<id>', views.edit_task),
    path('delete_task/<id>', views.delete_task),

]
    