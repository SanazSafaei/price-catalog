

class Article():

    def __init__(self, article_number: int = 0) -> None:
        self.article_number = article_number
        self.fields = []
        self.variations = []


    def add_varitaion(self, variation: dict):
        self.variations.append(variation)

    def set_fields(self, fields: dict):
        self.fields = fields

