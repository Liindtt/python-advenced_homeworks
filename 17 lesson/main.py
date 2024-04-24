import json
from pydantic import BaseModel, ValidationError, Field, field_validator


class Author(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    gender: str
    nationality: str

    @field_validator('gender')
    @classmethod
    def gender_must_be_male_or_female(cls, v):
        if v.lower() not in ["male", "female"]:
            raise ValueError("gender must be 'Male' or 'Female'!")
        return v.title()

    def __str__(self):
        return f"\n\tAuthor name: {self.name}\n\tGender: {self.gender}\n\tNationality: {self.nationality}\n"


class Book(BaseModel):
    id: int = Field(ge=1000, le=9999)
    title: str = Field(alias="nameBook")
    year: int = Field(ge=1970)
    authors: list[Author]

    def __str__(self):
        return (f"Book id: {self.id}\nTitle: {self.title}\nYear: {self.year}\nAuthors: "
                f"{''.join([str(author) for author in self.authors])}")

    @classmethod
    def load_data_from_json(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            return cls(**data)

    def save_data_to_json(self, filename):
        with open(filename, "w") as file:
            json.dump(self.dict(exclude={'id'}), file, indent=4)


try:
    # Loading data from file and saving it, then print a result
    book = Book.load_data_from_json("data.json")
    print(book)
except ValidationError as e:
    print(e.json())
else:
    # Changing year of book, then print a result
    book.year = 1998
    print(book)
    # Saving data in another file without "id"
    book.save_data_to_json("data_without_id.json")
