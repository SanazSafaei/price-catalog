import unittest
from src.mapper import Mapper


class TestMapper(unittest.TestCase):

    def test_generate_mapping(self):
        mapping_row = {
            'source': 'winter',
            'destination': 'Winter',
            'source_type': 'season',
            'destination_type': 'season'
            }
        mapper = Mapper('sample/mappings.csv')
        mapper_row = mapper.mapping[0]
        self.assertDictEqual(mapping_row, mapper_row)

    def test_empty_mapping(self):
        data = {
            'ean': '8719245200978',
            'supplier': 'Rupesco BV',
            'brand': 'Via Vai',
            'catalog_code': '',
            'collection': 'NW 17-18',
            'season': 'winter',
            'article_structure_code': '10',
            'article_number': '15189-02',
            'article_number_2': '15189-02 Aviation Nero',
            'article_number_3': 'Aviation',
            'color_code': '1',
            'size_group_code': 'EU',
            'size_code': '38',
            'size_name': '38',
            'currency': 'EUR',
            'price_buy_gross': '',
            'price_buy_net': '58.5',
            'discount_rate': '',
            'price_sell': '139.95',
            'material': 'Aviation',
            'target_area': 'Woman Shoes'
            }
        mapper = Mapper('sample/mappings.csv')
        mapper.MAPPING = {}
        mapped_data = mapper.map(data)
        self.assertDictEqual(mapped_data, data)

    def test_map(self):
        data = {
            'ean': '8719245200978',
            'supplier': 'Rupesco BV',
            'brand': 'Via Vai',
            'catalog_code': '',
            'collection': 'NW 17-18',
            'season': 'winter',
            'article_structure_code': '10',
            'article_number': '15189-02',
            'article_number_2': '15189-02 Aviation Nero',
            'article_number_3': 'Aviation',
            'color_code': '1',
            'size_group_code': 'EU',
            'size_code': '38',
            'size_name': '38',
            'currency': 'EUR',
            'price_buy_gross': '',
            'price_buy_net': '58.5',
            'discount_rate': '',
            'price_sell': '139.95',
            'material': 'Aviation',
            'target_area': 'Woman Shoes'
            }

        response = {
            'ean': '8719245200978',
            'supplier': 'Rupesco BV',
            'brand': 'Via Vai',
            'catalog_code': '',
            'collection': 'Winter Collection 2017/2018',
            'season': 'Winter',
            'article_structure_code': '10',
            'article_structure': 'Pump',
            'article_number': '15189-02',
            'article_number_2': '15189-02 Aviation Nero',
            'article_number_3': 'Aviation',
            'color': 'Nero', 
            'color_code': '1',
            'size_group_code': 'EU',
            'size': 'European size 38',
            'size_code': '38',
            'size_name': '38',
            'currency': 'EUR',
            'price_buy_gross': '',
            'price_buy_net': '58.5',
            'discount_rate': '',
            'price_sell': '139.95',
            'material': 'Aviation',
            'target_area': 'Woman Shoes',
            'price_buy_net_currency': '58.5 EUR'
        }

        mapper = Mapper('sample/mappings.csv')
        mapped_data = mapper.map(data)
        self.assertDictEqual(mapped_data, response)

    def test_empty_input_map(self):
        data = {}
        response = None
        mapper = Mapper('sample/mappings.csv')
        mapped_data = mapper.map(data)
        self.assertEqual(mapped_data, response)
