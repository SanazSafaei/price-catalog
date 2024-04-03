from argparse import ArgumentParser
from price_catalog import PriceCatalog
from convert_to_json import ConverToJson

class Main():

    def main(self):
        """execution of program"""

        parser = self.define_input_arguments()
        input_args = parser.parse_args()

        price_cat = PriceCatalog(input_args.file_path, input_args.mapper_path)
        catalaog = price_cat.create_catalog(input_args.article_identifier)
        ConverToJson().convert_catalog_to_json(catalaog)

    def define_input_arguments(self) -> ArgumentParser:
        """defines inputs and main --help fields"""

        parser = ArgumentParser(description='Process catlog csv data and convert it to json file.')
        parser.add_argument('-f', '--filename', dest='file_path', type=str, default='pricat.csv',
                            help='Path of data file. sample /dir/pricat.csv')
        parser.add_argument('-m','--mapper', dest='mapper_path',type=str, default='mappings.csv',
                            help='Path of mapping file. sample /dir/mapping.csv')
        parser.add_argument('-a' ,'--article_identifier', dest='article_identifier',
                            type=str, default='article_number',
                            help='Path of mapping file. sample article_identifier')

        return parser


if __name__ == '__main__':
    Main().main()
