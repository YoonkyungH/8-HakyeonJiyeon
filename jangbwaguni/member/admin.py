from django.contrib import admin
from .models import Customer, Rider

from orderrequest.models import OrderApply

class OrderApplyInline(admin.StackedInline):
    model = OrderApply
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    inlines = [OrderApplyInline]

class RiderAdmin(admin.ModelAdmin):
    inlines = [OrderApplyInline]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Rider, RiderAdmin)

