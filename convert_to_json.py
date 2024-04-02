import json
from catalog import Catalog

class ConverToJson():
    """converts objects to a json object."""

    def convert_catalog_to_json(self, catalog: Catalog):
        """converts  Catlog object to a json object."""

        json_data = catalog.fields.copy()

        json_data['articles'] = []
        for article in catalog.articles:
            article_data = article.fields.copy()
            article_data['variations'] = article.variations
            json_data['articles'].append(article.fields | {'variation': article.variations})

        with open("json_price_catalog.json", "w", encoding="utf-8") as file:
            json.dump(json_data, file)
