from price_catalog import PriceCatalog
from convert_to_json import ConverToJson


def main():

    price_cat = PriceCatalog('pricat.csv')
    catalaog = price_cat.create_catalog('article_number')
    ConverToJson().convert_catalog_to_json(catalaog)
    return

if __name__ == '__main__':
    main()
