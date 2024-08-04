
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = []
    # email = models.EmailField()
    email=None

    # unique 임시 해제
    nickname = models.CharField(max_length=100,default="")



