from django.contrib import admin

from .models import orders
from member.models import Rider
admin.site.register(orders)
admin.site.register(Rider)