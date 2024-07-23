from models import ArticleModel


class ArticleController:
    def __init__(self):
        self.articles = []

    def add_article(self, title: str, author: str, year: int):
        article = ArticleModel(title, author, year)
        self.articles.append(article)

    def print_articles(self):
        return self.articles

    def remove_article(self,  index: int):
        if 0 <= index < len(self.articles):
            self.articles.pop(index)
        else:
            return None

    def update_article(self, index: int, title: str = None, author: str = None, year: int = None):
        if 0 <= index < len(self.articles):
            if title:
                self.articles[index].title = title
            if author:
                self.articles[index].author = author
            if year:
                self.articles[index].year = year
            return self.articles[index]
        else:
            return None
