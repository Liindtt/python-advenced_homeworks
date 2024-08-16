from django.shortcuts import render
from .data import films_list


def home(request):
    # Отримуємо параметри запиту
    sort_param = request.GET.get('sort')

    if sort_param:
        try:
            key, order = sort_param.split(':')
            if key in ['id', 'title', 'year', 'genre'] and order in ['asc', 'desc']:
                # Сортуємо список фільмів за заданим ключем і порядком
                reverse = True if order == 'desc' else False
                sorted_films = sorted(films_list, key=lambda x: x[key], reverse=reverse)
            else:
                sorted_films = films_list  # Якщо параметри некоректні, ігноруємо їх
        except ValueError:
            sorted_films = films_list  # Якщо параметри некоректні, ігноруємо їх
    else:
        sorted_films = films_list  # Якщо параметри відсутні, показуємо всі фільми без сортування

    return render(request, 'films/home.html', {'films_list': sorted_films, "title": "Home page"})


def film_detail(request, id):
    # Знайдіть фільм за його ID
    film = next((film for film in films_list if film["id"] == id), None)
    print(film)
    if not film:
        # Якщо фільм не знайдений, повертаємо 404
        return render(request, 'films/404.html', status=404)

    return render(request, 'films/film_detail.html', {'film': film})


def filter_film(request):
    genre = request.GET.get('genre')
    year = request.GET.get('year')
    filtered_films = []
    for film in films_list:
        if film["genre"] == genre and film["year"] == int(year):
            filtered_films.append(film)
            print(film)
    print(genre, year)
    print(filtered_films)
    if not filtered_films:
        return render(request, "films/404.html", status=404)

    return render(request, "films/home.html", {"films_list": filtered_films, "title": "Filtered films"})


def filter_form(request):
    return render(request, 'films/filter_form.html')

