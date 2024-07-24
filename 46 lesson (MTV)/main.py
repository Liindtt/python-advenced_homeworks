from models import ArticleModel
from views import ArticleView
from templates import ArticlesTemplateTable, ArticlesTemplateSimple
from faker import Faker
from random import randint

model = ArticleModel()
view = ArticleView()
template_table = ArticlesTemplateTable()
template_simple = ArticlesTemplateSimple()
fake = Faker(locale="uk_UA")

while True:
    choice = view.print_menu()
    match choice:
        case 1:
            title, author, year = (fake.text(max_nb_chars=20), fake.first_name() + " " + fake.last_name(),
                                   randint(2000, 2024))
            model.add_article(title, author, year)
        case 2:
            articles = model.get_articles()
            template_choice = input("Choose template (table/simple): ")
            if template_choice.lower().rstrip() == "table":
                template_table.show_articles(articles)
            elif template_choice.lower().rstrip() == "simple":
                template_simple.show_articles(articles)
            else:
                print("Wrong answer!")
        case 3:
            index = view.get_article_index()
            title, author, year = view.get_article_details()
            model.update_article(index, title=title, author=author, year=year)
        case 4:
            index = view.get_article_index()
            model.remove_article(index)
        case 5:
            break
