from django import forms
from .models import Computer


class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = [
            'pc_name',
            'cpu_type',
            'cpu_series',
            'cpu_model',
            'clock_speed',
            'gpu_type',
            'gpu_model',
            'gpu_ram',
            'ram_type',
            'ram_size',
            'disk_type',
            'disk_value',
            'in_stock',
            'manufacture_date',
            'description',
            'image'
        ]

        # Валідація тактової частоти
        def clean_clock_speed(self):
            data = self.cleaned_data['clock_speed']
            if data < 0:
                raise forms.ValidationError("Тактова частота не може бути від’ємною!")
            return data