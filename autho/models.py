from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    """
    Django требует, чтобы кастомные пользователи определяли свой собственный
    класс Manager. Унаследовавшись от BaseUserManager, мы получаем много того
    же самого кода, который Django использовал для создания User (для демонстрации).
    """

    def create_user(self, email, password=None):
        """ Создает и возвращает пользователя с имэйлом, паролем и именем. """
        if email is None:
            raise TypeError('Users must have an email address.')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_admin = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = 'ADMIN'
    SUPER_ADMIN = 'SUPER_ADMIN'
    USER = 'USER'
    role_types = (
        (ADMIN, ADMIN),
        (SUPER_ADMIN, SUPER_ADMIN),
        (USER, USER)
    )
    email = models.EmailField(max_length=100, unique=True)
    is_admin = models.BooleanField(default=False)
    roles = models.CharField(
        choices=role_types, max_length=50, default=USER
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'

    def __str__(self):
        return f'{self.email}'


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='profile'
    )


class TokenLog(models.Model):
    """
    Token log model
    """
    user = models.ForeignKey(
        User,
        related_name='tokens',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=500)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return "token={0}".format(self.token)

    class Meta:
        index_together = [
            ["token", "user"]
        ]
        verbose_name = 'Токен'
        verbose_name_plural = 'Токены'
