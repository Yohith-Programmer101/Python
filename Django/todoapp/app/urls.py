from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('a', add_todo, name='add_todo'),
    path('d/<int:todo_id>/', delete_todo, name='delete_todo'),
]