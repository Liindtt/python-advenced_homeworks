class ArticleModel:
    def __init__(self, title: str, author: str, year_of_release: int):
        self.title = title
        self.author = author
        self.year_of_release = year_of_release

    def __str__(self):
        return f"Book title: '{self.title}', Author: {self.author}, Year of release: {self.year_of_release}"
