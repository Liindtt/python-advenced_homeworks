from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Computer
from .forms import ComputerForm


# Список всіх ПК
def computers_list(request):
    computers = Computer.objects.all()  # Отримуємо всі записи з бази даних
    return render(request, 'computers_list.html', {'computers': computers})


# Перегляд деталей конкретного ПК
def computer_detail(request, pk):
    computer = get_object_or_404(Computer, pk=pk)  # Отримуємо запис ПК або 404
    return render(request, 'computer_detail.html', {'computer': computer})


# Створення нового ПК
def create_computer(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST, request.FILES)  # Отримуємо дані з форми
        if form.is_valid():
            form.save()  # Зберігаємо новий ПК у базу
            messages.success(request, "Збірку ПК було успішно додано!")  # Повідомлення про успішне додавання ПК
            return redirect('computers_list')  # Переадресація на список ПК
        else:
            messages.error(request, "Некоректно введені дані")  # Повідомлення про помилку
    else:
        form = ComputerForm()
    return render(request, 'create_computer.html', {'form': form})


# Редагування існуючого ПК
def edit_computer(request, pk):
    computer = get_object_or_404(Computer, pk=pk)  # Отримуємо ПК для редагування
    if request.method == 'POST':
        form = ComputerForm(request.POST, request.FILES, instance=computer)
        if form.is_valid():
            form.save()  # Зберігаємо зміни
            messages.success(request, "Збірку ПК змінено!")  # Повідомлення про успішні зміни ПК
            return redirect('computers_list')  # Переадресація на список ПК
        else:
            messages.error(request, "Некоректно введені дані")  # Повідомлення про помилку
    else:
        form = ComputerForm(instance=computer)
    return render(request, 'edit_computer.html', {'form': form})


# Видалення ПК з підтвердженням
def delete_computer(request, pk):
    computer = get_object_or_404(Computer, pk=pk)  # Отримуємо ПК для видалення
    if request.method == 'POST':
        computer.delete()  # Видаляємо ПК
        messages.success(request, "Збірку ПК видалено!")  # Повідомлення про видалення ПК
        return redirect('computers_list')  # Переадресація на список ПК
    return render(request, 'delete_computer_confirm.html', {'computer': computer})


# Пошук ПК за виробником або іншим полем
def search_computer(request):
    query = request.GET.get('q')  # Отримуємо запит з форми пошуку
    results = Computer.objects.filter(manufacturer__icontains=query)  # Фільтрація за виробником
    return render(request, 'computers_list.html', {'computers': results})
