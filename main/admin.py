from django.contrib import admin
from .models import User2, Role, Permission, UserHasRole, RoleHasPermission

# Register your models here.
admin.site.register(User2)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(UserHasRole)
admin.site.register(RoleHasPermission)
