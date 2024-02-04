from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from Users.managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    telegram_id = models.CharField(max_length=20, null=True, blank=True,
                                   verbose_name="Telegram User ID Number")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


def get_expired_time():
    return timezone.now() + timezone.timedelta(hours=24)


class UserToken(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='tokens')
    token = models.CharField(max_length=24)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    has_expiration = models.BooleanField(default=False)
    expired_at = models.DateTimeField(default=get_expired_time, null=True, blank=True)

    def __str__(self):
        return self.user.email
