import unittest
from src.article import Article
from src.catalog import Catalog
from src.price_catalog import PriceCatalog


class TestPriceCatalog(unittest.TestCase):

    def test_initiate_price_catalog(self):

        pricCat = PriceCatalog('tests/test_pricat.csv', 'mappings.csv')
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
        self.assertEqual(pricCat.all_data, expected_output)

    def test_create_catalog(self):

        article1 = Article()
        article1.set_fields(
            {
                'article_number': '1-1',
            }
        )
        article1.add_varitaion(
            {
                'ean': '978',
                'size_code': '38',
                'size': 'European size 38',
                'color_code': '1',
                'color': 'Nero'
            }
        )
        article1.add_varitaion(
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
        article2.add_varitaion(
            {
                'ean': '980',
                'size_code': '40',
                'size': 'European size 40',
                'color_code': '3',
                'color': 'Brandy Nero'
            }
        )
        article2.add_varitaion(
            {
                'ean': '981',
                'size_code': '40',
                'size': 'European size 40',
                'color_code': '3',
                'color': 'Brandy Nero'
            }
        )

        expected_catlog = Catalog()
        expected_catlog.set_fields(
            {
                'supplier': 'Rupesco BV',
                'size_group_code': 'EU',
            }
        )
        expected_catlog.add_articles(article1)
        expected_catlog.add_articles(article2)

        pricCat = PriceCatalog('tests/test_pricat.csv', 'mappings.csv')
        catlog = pricCat.create_catalog('article_number')

        self.assertIsInstance(catlog, Catalog)
        self.assertDictEqual(catlog.fields, expected_catlog.fields)
        self.assertEqual(len(catlog.articles), len(expected_catlog.articles))

        for i, article_output in enumerate(catlog.articles):
            self.assertEqual(article_output.fields, expected_catlog.articles[i].fields)
            self.assertEqual(article_output.variations, expected_catlog.articles[i].variations)
        