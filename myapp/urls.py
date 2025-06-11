from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('ToDo/', ToDo, name='ToDo'),
    path('insert/', insert, name='insert'), 
    path('update/<int:id>', edit, name='edit'),
    path('delete/<int:id>', delete, name='delete')
]