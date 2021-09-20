from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager


class User(AbstractBaseUser):

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(validators=[validators.validate_email], unique=True, blank=False)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_superuser = models.BooleanField(default=False)  # a superuser
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = UserManager()

    def __str__(self):
        return self.username
