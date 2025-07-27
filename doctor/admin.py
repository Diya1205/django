from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'contact', 'availability')
    list_filter = ('specialty', 'availability')
    search_fields = ('name', 'specialty')
    ordering = ['name']
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'specialty')
        }),
        ('Contact & Availability', {
            'fields': ('contact', 'availability')
        }),
    )