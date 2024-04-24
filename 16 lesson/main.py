import json
import pickle


class Author:
    def __init__(self, name: str, gender: str, nationality: str):
        self.name = name
        self.gender = gender
        self.nationality = nationality

    def __str__(self):
        return f"\n\tName: {self.name}\n\tGender: {self.gender}\n\tNationality: {self.nationality}\n"


class Book:
    def __init__(self, title: str, year: int, authors: list) -> None:
        self.title = title
        self.year = year
        self.authors = authors

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "authors": [
                {
                    "name": author.name,
                    "gender": author.gender,
                    "nationality": author.nationality,
                } for author in self.authors
            ]
        }

    def show_book_info(self):
        print(f"Title: {self.title}\nYear: {self.year}\nAuthors: {"".join([str(author) for author in self.authors])}")

    def save_to_json(self):
        with open("sample.json", "w") as file:
            json.dump(self.to_dict(), file, indent=4)

    @staticmethod
    def load_from_json():
        with open("sample.json", "r") as file:
            data = json.load(file)
            new_title = data["title"]
            new_year = data["year"]
            new_authors = [Author(author['name'], author["gender"], author["nationality"]) for author in data["authors"]]
            return Book(new_title, new_year, new_authors)

    def save_to_pickle(self):
        with open("sample.txt", "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_pickle():
        with open("sample.txt", "rb") as file:
            data = pickle.load(file)
            return data


# Main program
author1 = Author("J.K. Rowling", "Female", "British")
author2 = Author("Stephen King", "Male", "American")
book1 = Book("Harry Potter", 1997, [author1, author2])

# Show info about book
print("Дані екземпляра book1: ")
book1.show_book_info()
# Save book1's info in file using json
book1.save_to_json()
print()

# Creating new book obj
new_book = Book.load_from_json()
# Checking a data from new obj
print("Отримуємо дані з файлу, за допомогою json:")
new_book.show_book_info()
print()

# Save book1's info in file using pickle
book1.save_to_pickle()
# Load a data from file using pickle
data_from_pickle = Book.load_from_pickle()
print("Отримуємо дані з файлу, за допомогою pickle:")
print(data_from_pickle.show_book_info())
