import json
import unittest
from catalog import Catalog
from article import Article
from convert_to_json import ConverToJson


class TestConverToJson(unittest.TestCase):


    def test_convert_catalog_to_json(self):

        article = Article()
        article.set_fields(
            {
                'article_field_1': 3,
                'article_field_2': 4
            }
        )
        article.add_varitaion(
            {
                'varitation_field_1': 5,
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
                            'varitation_field_1': 5,
                            'variation_field_2': 6
                            }
                        ]
                    }
                ]
            }
        }

        file_path = 'test_successful_convert_catlog_to_json'
        ConverToJson().convert_catalog_to_json(catalog, file_path)
        with open(file_path+'.json', 'r', encoding= "utf-8") as output_data:
            real_json_output = json.load(output_data)

        self.assertDictEqual(except_json_converted_output, real_json_output)

    def test_conver_empty_article_to_json(self):

        with self.assertRaises(TypeError):
            catalog = Catalog()
            file_path = 'test_successful_convert_catlog_to_json'
            ConverToJson().convert_catalog_to_json(catalog, file_path)