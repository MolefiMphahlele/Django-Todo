
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('New-Task/', views.TaskCreation, name='TaskCreate'),
    path('Update-Task/<int:task_id>', views.TaskUpdate, name ="Update"),
    path('Delete-Task/<int:task_id>', views.TaskDelete, name='Delete'),
]