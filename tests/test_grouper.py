import unittest
from src.grouper import Grouper


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
            'common_field_3': {'field_1':1, 'field_2':2}
        }

        grouped_common = Grouper(input_data).find_common_fields_with_values()

        self.assertDictEqual(expected_group_field, grouped_common)

    def test_empty_list_in_find_common_field(self):
        input_data = []

        grouped_common = Grouper(input_data).find_common_fields_with_values()

        self.assertDictEqual({}, grouped_common)

    def test_bad_structure_in_find_common_field(self):

        with self.assertRaises(ValueError):
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

    def test_grouped_data_by_spesefic_field(self):

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
                'field_3': 3,
                'field_4': 6,
                'field_6': {4:5}
            },
            {
                'common_field_1': 1,
                'common_field_2': 2,
                'common_field_3': {'field_1':1, 'field_2':2},
                'field_3': 4,
                'field_4': 8,
                'field_6': {9:10}
            }
        ]

        expected_output = {
            3: [
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
                'field_3': 3,
                'field_4': 6,
                'field_6': {4:5}
            }
            ],
            4: [
                {
                    'common_field_1': 1,
                    'common_field_2': 2,
                    'common_field_3': {'field_1':1, 'field_2':2},
                    'field_3': 4,
                    'field_4': 8,
                    'field_6': {9:10}
                }
            ]
        }

        grouped_data, common_fields = Grouper(input_data).group_by_spesefic_field('field_3')
        
        self.assertDictEqual(grouped_data, expected_output)

    def test_common_fields_in_group_by_spesefic_field(self):

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
                'field_3': 3,
                'field_4': 6,
                'field_6': {4:5}
            },
            {
                'common_field_1': 6,
                'common_field_2': 4,
                'common_field_3': {'field_1':3, 'field_2':4},
                'field_3': 4,
                'field_4': 8,
                'field_6': {9:10}
            },
            {
                'common_field_1': 6,
                'common_field_2': 7,
                'common_field_3': {'field_1':3, 'field_2':4},
                'field_3': 4,
                'field_4': 8,
                'field_6': {9:10}
            }
        ]

        expected_output = {
                'common_field_1': {3: 1, 4:6},
                'common_field_3': {3: {'field_1':1, 'field_2':2}, 4: {'field_1':3, 'field_2':4}},
                'field_3': {3: 3 ,4: 4}
        }

        grouped_data, common_fields = Grouper(input_data).group_by_spesefic_field('field_3')
        
        self.assertDictEqual(common_fields, expected_output)

    def test_empty_list_in_group_by_spesefic_field(self):

        input_data = []
        expected_output = {}
        grouped_data, common_fields = Grouper(input_data).group_by_spesefic_field('field_3')
        
        self.assertDictEqual(common_fields, expected_output)
        self.assertDictEqual(grouped_data, expected_output)

    def test_bad_structure_in_group_by_spesefic_field(self):
        with self.assertRaises(ValueError):
            input_data = [
                {
                    'common_field_1': 1,
                    'common_field_2': 2,
                    'common_field_3': {'field_1':1, 'field_2':2},
                    'field_3': 3,
                    'field_4': 5,
                    'field_6': {1:10}
                    },
                []
            ]
            grouped_data, common_fields = Grouper(input_data).group_by_spesefic_field('field_3')

    def test_not_available_identifire_in_group_by_spesefic_field(self):
        
        with self.assertRaises(ValueError):
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
                    'field_4': 5,
                    'field_6': {1:10}

                }
            ]
            grouped_data, common_fields = Grouper(input_data).group_by_spesefic_field('field_3')



