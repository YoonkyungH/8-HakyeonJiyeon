from django.contrib import admin

from .models import Customer
admin.site.register(Customer)

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('cus_id', )

# admin.site.register(user, UserAdmin)
