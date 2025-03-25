from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, email, name, mobile, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        if not mobile:
            raise ValueError("The Mobile field must be set.")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, mobile, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email=email, name=name, mobile=mobile, password=password, **extra_fields)


class User(AbstractUser):
    username = None  # Remove the username field
    email = models.EmailField(unique=True)
    mobile = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format: '+999999999'."
        )], default=+9999999999
    )
    name = models.CharField(max_length=255)  # Add name field

    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = ['name', 'mobile']

    objects = UserManager()  # Link to the custom UserManager

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        self.email = self.email.lower()  # Ensure email is stored in lowercase


class Task(models.Model):
    TASK_TYPES = (('PERSONAL', 'Personal'), ('WORK', 'Work'))
    STATUSES = (('PENDING', 'Pending'), ('COMPLETED', 'Completed'))

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=20, choices=TASK_TYPES, default='PERSONAL')
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUSES, default='PENDING')
    assigned_to = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name
