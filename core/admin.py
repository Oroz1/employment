from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from .models import *



class UserAdminConfig(UserAdmin):
    model = Users
    search_fields = ('id', 'username', 'first_name', 'last_name', 'phone_number', 'email')
    list_display = ('id', 'username', 'get_avatar', 'first_name', 'last_name', 'phone_number', 'email', 'last_login')
    list_display_links = ('id', 'first_name', 'last_name', 'username',)
    fieldsets = (
        (None, {'fields': (
                'avatar',
                'get_avatar',
                'username',
                'first_name', 
                'last_name', 
                'email',
                'gender',
                'date_of_birth',
                'phone_number', 
                'is_superuser',
                'password',
                'created_at',
                'updated_at',
            )},
         ),
    )
    add_fieldsets = (
        (None, {
            'fields': (
                'avatar',
                'username',
                'first_name', 
                'last_name',
                'email',
                'phone_number',
                'gender',
                'date_of_birth',
                'password1',
                'password2',
                'is_superuser',
            )}
         ),
    )
    readonly_fields = ('last_login', 'get_avatar', 'created_at', 'updated_at',)


    def get_avatar(self, obj):
        try:
            return mark_safe(f'<img src="{obj.avatar.url}" width="50rem">')
        except Exception:
            return mark_safe(f'-')

    get_avatar.short_description = 'Аватарка'


admin.site.register(Users, UserAdminConfig)

# Register your models here.
