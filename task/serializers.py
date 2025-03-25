from rest_framework import serializers
from .models import Task, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile', 'password']  # Include fields for user creation
        extra_kwargs = {
            'password': {'write_only': True}  # Password should not be exposed in responses
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password before saving
        user.save()
        return user


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'task_type', 'status', 'created_at']


class TaskAssignSerializer(serializers.Serializer):
    user_ids = serializers.ListField(child=serializers.IntegerField())

    def validate_user_ids(self, value):
        if not User.objects.filter(id__in=value).exists():
            raise serializers.ValidationError("Invalid user IDs")
        return value


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']

    def validate_status(self, value):
        if value not in ['PENDING', 'COMPLETED']:
            raise serializers.ValidationError("Invalid status value.")
        return value
