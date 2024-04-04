from file_manager import FileManager
from mapper import Mapper
from grouper import Grouper
from catalog import Catalog
from article import Article

class PriceCatalog():
    """recives a price catlog csv adress and generates a catlog object."""

    all_data = []

    def __init__(self, catlog_data_file_address: str, mapping_file_address: str) -> None:
        self.catalog_file = FileManager(catlog_data_file_address)
        self.mapping_file_address = mapping_file_address
        self._map_all_data()


    def _map_all_data(self) -> None:
        """generating catalog mapped data."""

        self.all_data = []
        mapper = Mapper(self.mapping_file_address)
        while x := self.catalog_file.get_row_data():
            self.all_data.append(mapper.map(x))


    def create_catalog(self, article_identifire_field: str) -> Catalog:
        """generates a catlog object."""

        catalog = Catalog()
        grouper = Grouper(self.all_data)
        catalog_fields = grouper.find_common_fields_with_values()
        catalog.set_fields(catalog_fields)

        #create articles, article fields and append it to catlog
        articles, all_article_catlog_fields = grouper.group_by_spesefic_field(article_identifire_field)
        article_fileds_name_list = set(all_article_catlog_fields.keys()) - set(catalog_fields.keys())

        for article_identifire_value, variations in articles.items():

            article_obj = Article(article_number=article_identifire_value)

            article_fields = {field_name: all_article_catlog_fields[field_name][article_identifire_value] for field_name in article_fileds_name_list}

            article_obj.set_fields(article_fields)

            for variation in variations:
                #remove common fields
                for commo_field in all_article_catlog_fields:
                    variation.pop(commo_field)

                article_obj.add_varitaion(variation)

            catalog.add_articles(article_obj)

        return catalog

