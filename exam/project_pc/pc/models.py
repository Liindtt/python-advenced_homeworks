from django.contrib.auth.models import User
from django.db import models


class RamSize(models.Model):
    size = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.size}GB"


class RamType(models.Model):
    type = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return f"{self.type}"


class Computer(models.Model):
    CPU_TYPE_CHOICES = [
        ('Intel', 'Intel'),
        ('AMD', 'AMD'),
    ]

    CPU_SERIES_CHOICES = [
        ('Core i3', 'Core i3'),
        ('Core i5', 'Core i5'),
        ('Core i7', 'Core i7'),
        ('Core i9', 'Core i9'),
        ('Ryzen 3', 'Ryzen 3'),
        ('Ryzen 5', 'Ryzen 5'),
        ('Ryzen 7', 'Ryzen 7'),
        ('Ryzen 9', 'Ryzen 9'),
    ]

    GPU_TYPE_CHOICES = [
        ('GeForce RTX', 'GeForce RTX'),
        ('GeForce GTX', 'GeForce GTX'),
        ('Radeon RX', 'Radeon RX'),
    ]

    DICK_TYPE_CHOICES = [
        ('SSD', 'SSD'),
        ('HDD', 'HDD'),
        ('M2', 'M2'),

    ]

    pc_name = models.CharField(verbose_name='Назва збірки', max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    cpu_type = models.CharField(verbose_name='Тип процесора', max_length=100, choices=CPU_TYPE_CHOICES)
    cpu_series = models.CharField(verbose_name='Серія процесора', max_length=100, choices=CPU_SERIES_CHOICES)
    cpu_model = models.CharField(verbose_name='Модель процесора', max_length=7)
    clock_speed = models.DecimalField(verbose_name='Тактова частота', max_digits=5, decimal_places=2)  # Наприклад, 3.60 ГГц
    gpu_type = models.CharField(verbose_name='Тип відеокарти', max_length=100, choices=GPU_TYPE_CHOICES)
    gpu_model = models.CharField(verbose_name='Модель відеокарти', max_length=6)
    gpu_ram = models.CharField(verbose_name='Кількість відеопам\'яті', max_length=6)
    ram_type = models.ForeignKey(verbose_name='Тип ОЗП', to=RamType, on_delete=models.CASCADE)
    ram_size = models.ForeignKey(verbose_name='Кількість ОЗП', to=RamSize, on_delete=models.CASCADE)
    disk_type = models.CharField(verbose_name='Накопичувач', max_length=3, choices=DICK_TYPE_CHOICES)
    disk_value = models.IntegerField(verbose_name='Ємність', )
    in_stock = models.BooleanField(verbose_name='Наявність', default=True)
    manufacture_date = models.DateField(verbose_name='Дата виготовлення', )
    description = models.TextField(verbose_name='Опис для збірки', max_length=500, null=True)
    image = models.ImageField(verbose_name='Фото', upload_to='computers/', blank=True, null=True)  # Поле для картинки

    def __str__(self):
        return f"{self.pc_name} - {self.cpu_type} - {self.gpu_type} - {self.ram_size}"

