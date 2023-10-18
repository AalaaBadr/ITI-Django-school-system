from django.urls import path

from .views import *

urlpatterns = [
    # path('list', list_trainees, name='list_trainees'),
    path('list', ListTrainees.as_view(), name='list_trainees'),
    # path('add', add_trainee, name='add_trainee'),
    path('add', AddTrainee.as_view(), name='add_trainee'),
    path('update/<int:id>', update_trainee, name='update_trainee'),
    path('delete/<int:id>', delete_trainee, name='delete_trainee'),
]
