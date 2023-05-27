from django.contrib import admin
from .models import Email

# Register your models here.

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['recipient', 'subject', 'body', 'opened', 'sent_date', 'tracking_url']
    fieldsets = [
        ('Email Details', {'fields': ['recipient', 'subject', 'body', 'opened', 'sent_date', 'tracking_url']}),
    ]
