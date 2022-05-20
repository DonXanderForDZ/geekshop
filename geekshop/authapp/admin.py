from django.contrib import admin
from .models import ShopUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(ShopUser)
class ShooUserAdmin(UserAdmin):

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return [
            *super().get_fieldsets(request, obj),
            ('Custom fields', {'fields': ('city',)})
        ]
