from django.urls import path
from .import views

app_name = 'todolist'

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/<int:t_id>/', views.todo, name='todo'),
    path('addtodo/', views.add_todo, name='add_todo'),
    path('edit/<int:t_id>/', views.edit, name='edit'),
    
]