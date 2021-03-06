# Generated by Django 3.2.12 on 2022-05-24 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('roles', models.CharField(choices=[('ADMIN', 'ADMIN'), ('SUPER_ADMIN', 'SUPER_ADMIN'), ('USER', 'USER')], default='USER', max_length=50)),
            ],
            options={
                'verbose_name': 'Юзер',
                'verbose_name_plural': 'Юзеры',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TokenLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('token', models.CharField(max_length=500)),
                ('deleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Токен',
                'verbose_name_plural': 'Токены',
                'index_together': {('token', 'user')},
            },
        ),
    ]
