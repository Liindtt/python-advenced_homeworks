import requests
import json
from pydantic import BaseModel


class Book(BaseModel):
    number: int
    originalTitle: str
    releaseDate: str


def save_to_json(self, filename: str):
    with open(filename + '.json', "w") as file:
        json.dump(self, file, indent=4)


def get_data():
    resp = requests.get("https://potterapi-fedeperin.vercel.app/en/books")
    return resp.json()


books = get_data()
items = []

for book in books:
    item = Book(**book)
    items.append(item.dict())

save_to_json(items, "data")
