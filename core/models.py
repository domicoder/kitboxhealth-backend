from django.contrib.auth.models import AbstractUser

from common.models import AbstractBaseModel


class User(AbstractBaseModel, AbstractUser):
    def __str__(self):
        return self.username
