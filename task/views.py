from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task, User
from .serializers import UserSerializer, TaskCreateSerializer, TaskAssignSerializer, TaskDetailSerializer, \
    TaskStatusUpdateSerializer
from django.utils import timezone


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TaskAssignView(generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAssignSerializer

    def post(self, request, pk):
        task = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = User.objects.filter(id__in=serializer.validated_data['user_ids'])
        task.assigned_to.add(*users)
        return Response({'status': 'Users assigned successfully'}, status=status.HTTP_200_OK)


class UserTasksView(generics.ListAPIView):
    serializer_class = TaskDetailSerializer

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.kwargs['user_id'])


class TaskStatusUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskStatusUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        # Regular users can only update tasks assigned to them, admin can update all tasks
        if user.is_superuser:
            return Task.objects.all()
        return Task.objects.filter(assigned_to=user)

    def perform_update(self, serializer):
        # Check if the status is being updated to "COMPLETED"
        task_instance = self.get_object()  # Get the current task instance
        updated_status = serializer.validated_data.get('status')

        if updated_status == 'COMPLETED':
            task_instance.completed_at = timezone.now()

        serializer.save()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
