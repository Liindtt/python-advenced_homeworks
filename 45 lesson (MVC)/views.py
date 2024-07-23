class ArticleView:

    @staticmethod
    def print_menu():
        print("""=======================
| 1 - add article     |
| 2 - show article    |
| 3 - update article  |
| 4 - remove article  |
| 5 - exit            |
=======================""")
        return int(input("Choose any option: "))

    @staticmethod
    def show_articles(articles):
        for article in articles:
            print(article)
