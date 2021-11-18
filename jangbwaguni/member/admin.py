from django.contrib import admin

from .models import CustomUser
admin.site.register(CustomUser)

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('cus_id', )

# admin.site.register(user, UserAdmin)
