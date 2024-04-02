import unittest
from file_manager import FileManager


class TestFileManager(unittest.TestCase):

    def test_detect_first_line_fields(self):
        headline = ['source', 'destination', 'source_type', 'destination_type']
        self.assertEqual(headline, self.mapper_file.headlines)

    def test_error_on_empty_file(self):

        with self.assertRaises(ValueError):
            FileManager('test.csv')

    def test_row_data(self):
        data = {
            'source': 'winter',
            'destination': 'Winter',
            'source_type': 'season',
            'destination_type': 'season'
            }
        self.assertDictEqual(data, self.mapper_file.get_row_data())

    def setUp(self) -> None:
        self.mapper_file = FileManager('mappings.csv')
        return super().setUp()

    def tearDown(self):
        self.mapper_file.file.close()


if __name__ == '__main__':
    unittest.main()
