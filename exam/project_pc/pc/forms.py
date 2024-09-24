from django import forms
from .models import Computer


class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['manufacturer', 'cpu_type', 'clock_speed', 'ram_size', 'in_stock', 'manufacture_date', 'image']
