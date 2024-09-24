from django.db import models

class RAM(models.Model):
    size = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.size

class Computer(models.Model):
    MANUFACTURER_CHOICES = [
        ('Dell', 'Dell'),
        ('HP', 'HP'),
        ('Lenovo', 'Lenovo'),
        # Додати інші фірми
    ]

    CPU_CHOICES = [
        ('Intel', 'Intel'),
        ('AMD', 'AMD'),
        # Інші типи процесорів
    ]

    manufacturer = models.CharField(max_length=100, choices=MANUFACTURER_CHOICES)
    cpu_type = models.CharField(max_length=100, choices=CPU_CHOICES)
    clock_speed = models.DecimalField(max_digits=5, decimal_places=2)  # Наприклад, 3.60 ГГц
    ram_size = models.ForeignKey(RAM, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)
    manufacture_date = models.DateField()
    image = models.ImageField(upload_to='computers/', blank=True, null=True)  # Поле для картинки

    def __str__(self):
        return f"{self.manufacturer} - {self.cpu_type} ({self.clock_speed} GHz)"

