import unittest
from grouper import Grouper


class TestGrouper(unittest.TestCase):

    def test_find_common_field_in_list(self):

        input_data = [
            {
                'common_field_1': 1,
                'common_field_2': 2,
                'common_field_3': {'field_1':1, 'field_2':2},
                'field_3': 3,
                'field_4': 5,
                'field_6': {1:10}

            },
            {
                'common_field_1': 1,
                'common_field_2': 2,
                'common_field_3': {'field_1':1, 'field_2':2},
                'field_3': 4,
                'field_4': 6,
                'field_6': {4:5}
            }
        ]

        expected_group_field = {
            'common_field_1': 1,
            'common_field_2': 2,
            'common_field_3': {'field_1':1, 'field_2':2},
        }

        grouped_common = Grouper(input_data).find_common_fields_with_values()

        self.assertDictEqual(expected_group_field, grouped_common)

    def test_find_common_field_in_empty_list(self):
        input_data = []

        grouped_common = Grouper(input_data).find_common_fields_with_values()

        self.assertDictEqual({}, grouped_common)

    def test_find_common_field_in_wrong_data_structure(self):

        input_data = [
            {
                'common_field_1': 1,
                'common_field_2': 2,
                'common_field_3': {'field_1':1, 'field_2':2},
                'field_3': 3,
                'field_6': {1:10}

            },
            {
                'common_field_1': 1,
                'common_field_2': 2,
                'common_field_3': {'field_1':1, 'field_2':2},
                'field_3': 4,
                'field_4': 6,
                'field_6': {4:5}
            },
            ['test']
        ]

        grouped_common = Grouper(input_data).find_common_fields_with_values()

        self.assertDictEqual({}, grouped_common)



