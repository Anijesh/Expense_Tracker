from django.contrib import admin

from .models import CurrentBalance,TrackingHistory,RequestLogs

admin.site.site_header = 'Expense Tracker'
admin.site.site_title ='Expense Tracker'
admin.site.site_url= 'Expense Tracker'


# Register your models here.

# admin.site.disable_action("delete_selected")

@admin.action(description="Mark selected transctions as Credit")
def make_credit(modeladmin, request, queryset):
    for q in queryset:
        if int(q.amount)<0:
            q.amount =q.amount*-1
        q.save()
    queryset.update(expense_type="CREDIT")


@admin.action(description='Mark selected transctions as Debit')
def make_debit(modeladmin,request,queryset):
    for q in queryset:
        if int(q.amount)>0:
            q.amount =q.amount*-1
        q.save()
    queryset.update(expense_type='DEBIT')

class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display=[
        'current_balance',
        'amount',
        'expense_type',
        'description',
        'created_at'
    ]
    search_fields=['expense_type','description']
    list_filter=['expense_type']
    ordering=['created_at']

    actions=[make_credit,make_debit]


admin.site.register(CurrentBalance)
admin.site.register(TrackingHistory,TrackingHistoryAdmin)
admin.site.register(RequestLogs)
