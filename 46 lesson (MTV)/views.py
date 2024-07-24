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
    def get_article_details():
        title = input("Enter title: ")
        author = input("Enter author: ")
        year = int(input("Enter year of release: "))
        return title, author, year

    @staticmethod
    def get_article_index():
        return int(input("Enter article index: "))
