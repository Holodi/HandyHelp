from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.views import LoginView


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',
    )

    class Meta(AbstractUser.Meta):
        permissions = (('custom_user_permissions', 'Custom User Permissions'),)

    # Змінюємо related_name для user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',
        help_text='Specific permissions for this user.',
        related_query_name="user",
    )


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    location = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
