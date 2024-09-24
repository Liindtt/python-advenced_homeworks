from django.contrib import admin
from .models import Computer, RAM


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'cpu_type', 'clock_speed', 'ram_size', 'in_stock', 'manufacture_date')
    search_fields = ['manufacturer', 'cpu_type']
    list_filter = ['manufacturer', 'cpu_type', 'ram_size', 'in_stock']


admin.site.register(Computer, ComputerAdmin)
admin.site.register(RAM)
