from django.contrib import admin

from .models import Rider, Customer#, OrderApply
admin.site.register(Rider)
admin.site.register(Customer)
#admin.site.register(OrderApply)