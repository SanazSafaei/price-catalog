from argparse import ArgumentParser
from src.price_catalog import PriceCatalog
from src.convert_to_json import ConvertToJson

class Main:

    def main(self):
        """execution of program"""

        parser = self.define_input_arguments()
        input_args = parser.parse_args()

        price_cat = PriceCatalog(input_args.file_path, input_args.mapper_path)
        catalog = price_cat.create_catalog(input_args.article_identifier)
        ConvertToJson().convert_catalog_to_json(catalog, input_args.json_file_name)

    def define_input_arguments(self) -> ArgumentParser:
        """defines inputs and main --help fields"""

        parser = ArgumentParser(description='Process catalog csv data and convert it to json file.')
        parser.add_argument('-f', '--filename', dest='file_path', type=str, default='sample/pricat.csv',
                            help='Path of data file. sample /dir/pricat.csv')
        parser.add_argument('-m','--mapper', dest='mapper_path',type=str, default='sample/mappings.csv',
                            help='Path of mapping file. sample /dir/mapping.csv')
        parser.add_argument('-a' ,'--article_identifier', dest='article_identifier',
                            type=str, default='article_number',
                            help='Path of mapping file. sample article_identifier')
        parser.add_argument('-n' ,'--json_file_name', dest='json_file_name',
                            type=str, default='sample/json_price_catalog.json',
                            help='Path of mapping file. sample json_response')

        return parser

