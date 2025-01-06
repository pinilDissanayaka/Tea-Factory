from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, UserManager
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")

        username = self.normalize_email(username)
        user = self.model(
            username=username, 
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    route_number=models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects=CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["route_number"]

class TeaLeaves(models.Model):
    quality=models.CharField(max_length=100)
    quantity=models.FloatField(max_length=50)
    description=models.TextField(max_length=100, blank=True, null=True)
    collector_at=models.DateTimeField(auto_now_add=True)
    collector_name=models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="collector_name")

