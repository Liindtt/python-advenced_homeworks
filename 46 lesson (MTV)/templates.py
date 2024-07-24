from abc import ABC, abstractmethod


class BaseTemplate(ABC):
    @abstractmethod
    def show_articles(self, articles):
        pass


class ArticlesTemplateTable(BaseTemplate):
    def show_articles(self, articles):
        print("Index | Title                | Author               | Year")
        print("-----------------------------------------------------------")
        for index, article in enumerate(articles):
            print(f"{index:<5} | {article['title']:<20} | {article['author']:<20} | {article['year_of_release']}")


class ArticlesTemplateSimple(BaseTemplate):
    def show_articles(self, articles):
        for index, article in enumerate(articles):
            print(f"{index + 1}. Title: {article['title']}, Author: {article['author']}, "
                  f"Year: {article['year_of_release']}")
