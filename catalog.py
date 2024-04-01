
class Catalog():

    def __init__(self) -> None:
        self.fields = []
        self.articles = []

    def add_articles(self, articles: dict):
        self.articles.append(articles)

    def set_fields(self, fields: dict):
        self.fields = fields
