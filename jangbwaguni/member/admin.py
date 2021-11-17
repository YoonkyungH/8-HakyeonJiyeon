from django.contrib import admin

from .models import Customer, Rider
admin.site.register(Customer)
admin.site.register(Rider)

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('cus_id', )

# admin.site.register(user, UserAdmin)
