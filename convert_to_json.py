import json
from catalog import Catalog

class ConverToJson():
    """converts objects to a json object."""

    DEFAULT_JSON_FILE_ADDRESS = 'json_price_catalog'

    def convert_catalog_to_json(
            self, catalog: Catalog,
            json_file_address: str = DEFAULT_JSON_FILE_ADDRESS):
        """converts  Catlog object to a json object."""

        json_data = {}
        json_data['Catalog'] = catalog.fields.copy()

        json_data['Catalog']['Articles'] = []
        for article in catalog.articles:
            # article_data = article.fields.copy()
            # article_data['Variation'] = article.variations
            json_data['Catalog']['Articles'].append(article.fields | {'Variations': article.variations})

        with open(json_file_address+".json", "w", encoding="utf-8") as file:
            json.dump(json_data, file)
