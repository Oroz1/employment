from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


MALE = 'M'
FEMALE = 'F'

GENDER = (
    (MALE, 'Мужской',),
    (FEMALE, 'Женский',),
)


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавление') 
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    class Meta:
        abstract = True


class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self, username, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Суперпользователь должен быть назначен is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Суперпользователь должен быть назначен is_superuser=True.')

        return self.create_user(username, name, password, **other_fields)

    def create_user(self, username, name, password, **other_fields):

        user = self.model(username=username, name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user



class Users(AbstractBaseUser, PermissionsMixin, TimeStampMixin):

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = 'пользователи'
        ordering = ('created_at', 'updated_at')
 
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='аватарка')
    username = models.CharField(max_length=20, unique=True, verbose_name='имя пользователя')
    name = models.CharField(max_length=150, verbose_name='полное имя')
    email = models.EmailField(verbose_name='элетронная почта')
    phone_number = models.CharField(max_length=15, verbose_name='номер телефона')
    gender = models.CharField(max_length=1, verbose_name='пол', choices=GENDER, default=MALE)
    date_of_birth = models.DateField(verbose_name='дата рождения', null=True)

    is_staff = models.BooleanField(default=True, verbose_name='статус сотрудника')
    is_active = models.BooleanField(default=True, verbose_name='подтверждение')
    is_superuser = models.BooleanField(default=False, verbose_name='статус администратора')
    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'phone_number']

    def __str__(self):
        return f'{self.username}'

