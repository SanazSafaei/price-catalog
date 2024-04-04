import json
import unittest
from src.dto.catalog import Catalog
from src.dto.article import Article
from src.convert_to_json import ConvertToJson


class TestConverToJson(unittest.TestCase):


    def test_convert_catalog_to_json(self):

        article = Article()
        article.set_fields(
            {
                'article_field_1': 3,
                'article_field_2': 4
            }
        )
        article.add_variation(
            {
                'variation_field_1': 5,
                'variation_field_2': 6
            }
        )

        catalog = Catalog()
        catalog.set_fields(
            {
                'catalog_field_1': 1,
                'catalog_field_2': 2
            }
        )
        catalog.add_articles(article)

        except_json_converted_output = {
            'Catalog': { 
                'catalog_field_1': 1,
                'catalog_field_2': 2,
                'Articles': [
                    {
                        'article_field_1': 3,
                        'article_field_2': 4,
                        'Variations': [
                            {
                            'variation_field_1': 5,
                            'variation_field_2': 6
                            }
                        ]
                    }
                ]
            }
        }

        file_path = 'tests/test_successful_convert_catalog_to_json.json'
        ConvertToJson().convert_catalog_to_json(catalog, file_path)
        with open(file_path, 'r', encoding= "utf-8") as output_data:
            real_json_output = json.load(output_data)

        self.assertDictEqual(except_json_converted_output, real_json_output)

    def test_convert_empty_article_to_json(self):

        with self.assertRaises(TypeError):
            catalog = Catalog()
            file_path = 'tests/test_successful_convert_catalog_to_json.json'
            ConvertToJson().convert_catalog_to_json(catalog, file_path)
