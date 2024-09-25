from django.contrib import admin
from .models import Computer, RamSize, RamType


# Кастомізація моделі Computer
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('pc_name', 'cpu_type', 'cpu_series', 'gpu_type', 'in_stock')
    search_fields = ('pc_name', 'cpu_series', 'gpu_model')
    list_filter = ('cpu_type', 'gpu_type', 'ram_type', 'in_stock')
    ordering = ('-manufacture_date',)


admin.site.register(Computer, ComputerAdmin)
admin.site.register(RamSize)
admin.site.register(RamType)
