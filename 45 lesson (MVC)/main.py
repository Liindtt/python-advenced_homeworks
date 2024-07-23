from controllers import ArticleController
from views import ArticleView
from faker import Faker
from random import randint

controller = ArticleController()
view = ArticleView()
fake = Faker(locale="uk_UA")

while True:
    choice = view.print_menu()
    match choice:
        case 1:
            controller.add_article(fake.text(max_nb_chars=20), fake.full_name(), randint(2000, 2024))
        case 2:
            articles = controller.print_articles()
            view.show_articles(articles)
        case 3:
            controller.update_article(0, title="updated_article")
        case 4:
            controller.remove_article(1)
        case 5:
            break

