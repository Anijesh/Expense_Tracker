from django.contrib import admin

from .models import CurrentBalance,TrackingHistory,RequestLogs

# Register your models here.

admin.site.register(CurrentBalance)
admin.site.register(TrackingHistory)
admin.site.register(RequestLogs)
