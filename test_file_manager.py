import unittest
from file_manager import FileManager


class TestFileManager(unittest.TestCase):

    def test_head_lines(self):
        headline = ['source', 'destination', 'source_type', 'destination_type']
        mapper_file = FileManager('mappings.csv')
        self.assertEqual(headline, mapper_file.headlines)

    def test_empty_file(self):
        headline = None
        file = FileManager('test.csv')
        self.assertEqual(file.headlines, headline)

    def test_row_data(self):
        data = {
            'source': 'winter',
            'destination': 'Winter',
            'source_type': 'season',
            'destination_type': 'season'
            }
        mapper_file = FileManager('mappings.csv')
        self.assertDictEqual(data, mapper_file.get_row_data())


if __name__ == '__main__':
    unittest.main()
