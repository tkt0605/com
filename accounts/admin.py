from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ("username","email","active","staff","admin",)
    list_filter = ("admin","active",)
    filter_horizontal = ()
    ordering = ("email",)
    search_fields = ('email',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username',  'password1', 'password2')}
        ),
    )
    fieldsets = (
        (None, {'fields': ('email','username', 'password',)}),
        ('Permissions', {'fields': ('staff','admin',)}),
    )
    
admin.site.register(User, UserAdmin)