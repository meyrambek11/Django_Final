from django.contrib import admin

from autho.models import TokenLog, User, Profile
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_admin')
    fields = ('email', 'is_admin', 'roles')


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', )
    fields = ('user', )


@admin.register(TokenLog)
class TokenLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'deleted')
    fields = ('user', 'deleted', 'token')
