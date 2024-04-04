import unittest
from src.dto.article import Article
from src.dto.catalog import Catalog
from src.price_catalog import PriceCatalog


class TestPriceCatalog(unittest.TestCase):

    def test_initiate_price_catalog(self):

        pricat = PriceCatalog('tests/test_pricat.csv', 'sample/mappings.csv')
        expected_output = [
            {
                'ean': '978',
                'supplier': 'Rupesco BV',
                'article_number': '1-1',
                'color_code': '1',
                'size_group_code': 'EU',
                'size_code': '38',
                'size': 'European size 38',
                'color': 'Nero'
            }, 
            {
                'ean': '979',
                'supplier': 'Rupesco BV',
                'article_number': '1-1', 
                'color_code': '6',
                'size_group_code': 'EU',
                'size_code': '39',
                'size': 'European size 39',
                'color': 'Bosco Nero'
            },
            {
                'ean': '980',
                'supplier': 'Rupesco BV',
                'article_number': '1-2',
                'color_code': '3',
                'size_group_code': 'EU',
                'size_code': '40',
                'size': 'European size 40',
                'color': 'Brandy Nero'
            }, 
            {
                'ean': '981',
                'supplier': 'Rupesco BV',
                'article_number': '1-2',
                'color_code': '3',
                'size_group_code': 'EU',
                'size_code': '40',
                'size': 'European size 40',
                'color': 'Brandy Nero'
            }
        ]
        self.assertEqual(pricat.all_data, expected_output)

    def test_create_catalog(self):

        article1 = Article()
        article1.set_fields(
            {
                'article_number': '1-1',
            }
        )
        article1.add_variation(
            {
                'ean': '978',
                'size_code': '38',
                'size': 'European size 38',
                'color_code': '1',
                'color': 'Nero'
            }
        )
        article1.add_variation(
            {
                'ean': '979',
                'size_code': '39',
                'size': 'European size 39',
                'color_code': '6',
                'color': 'Bosco Nero'
            }
        )

        article2 = Article()
        article2.set_fields(
            {
                'article_number': '1-2',
            }
        )
        article2.add_variation(
            {
                'ean': '980',
                'size_code': '40',
                'size': 'European size 40',
                'color_code': '3',
                'color': 'Brandy Nero'
            }
        )
        article2.add_variation(
            {
                'ean': '981',
                'size_code': '40',
                'size': 'European size 40',
                'color_code': '3',
                'color': 'Brandy Nero'
            }
        )

        expected_catalog = Catalog()
        expected_catalog.set_fields(
            {
                'supplier': 'Rupesco BV',
                'size_group_code': 'EU',
            }
        )
        expected_catalog.add_articles(article1)
        expected_catalog.add_articles(article2)

        pricCat = PriceCatalog('tests/test_pricat.csv', 'sample/mappings.csv')
        catalog = pricCat.create_catalog('article_number')

        self.assertIsInstance(catalog, Catalog)
        self.assertDictEqual(catalog.fields, expected_catalog.fields)
        self.assertEqual(len(catalog.articles), len(expected_catalog.articles))

        for i, article_output in enumerate(catalog.articles):
            self.assertEqual(article_output.fields, expected_catalog.articles[i].fields)
            self.assertEqual(article_output.variations, expected_catalog.articles[i].variations)
        