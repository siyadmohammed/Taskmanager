from django.urls import path
from .views import TaskCreateView, TaskAssignView, UserTasksView, UserCreateView, TaskStatusUpdateView

urlpatterns = [
    path('tasks/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/assign/', TaskAssignView.as_view(), name='task-assign'),
    path('users/<int:user_id>/tasks/', UserTasksView.as_view(), name='user-tasks'),
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('tasks/<int:pk>/update-status/', TaskStatusUpdateView.as_view(), name='task-update-status'),
]
