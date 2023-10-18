from django.urls import path

from .views import *

urlpatterns = [
    # path('list', list_instructors, name='list_instructors'),
    path('list', ListInstructors.as_view(), name='list_instructors'),
    # path('add', add_instructor, name='add_instructor'),
    path('add', AddInstructor.as_view(), name='add_instructor'),
    path('update/<int:id>', update_instructor, name='update_instructor'),
    path('delete/<int:id>', delete_instructor, name='delete_instructor'),
]
