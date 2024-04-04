from src.file_manager import FileManager
from src.mapper import Mapper
from src.grouper import Grouper
from src.dto.catalog import Catalog
from src.dto.article import Article

class PriceCatalog:
    """recipes a price catalog csv address and generates a catalog object."""

    all_data = []

    def __init__(self, catalog_data_file_address: str, mapping_file_address: str) -> None:
        self.catalog_file = FileManager(catalog_data_file_address)
        self.mapping_file_address = mapping_file_address
        self._map_all_data()


    def _map_all_data(self) -> None:
        """generating catalog mapped data."""

        self.all_data = []
        mapper = Mapper(self.mapping_file_address)
        while line := self.catalog_file.get_row_data():
            self.all_data.append(mapper.map(line))


    def create_catalog(self, article_id_field: str) -> Catalog:
        """generates a catalog object."""

        catalog = Catalog()
        grouper = Grouper(self.all_data)
        catalog_fields = grouper.find_common_fields_with_values()
        catalog.set_fields(catalog_fields)

        #create articles, article fields and append it to catalog
        articles, all_article_catalog_fields = grouper.group_by_specific_field(article_id_field)
        article_fields_name_list = set(all_article_catalog_fields.keys()) - set(catalog_fields.keys())

        for article_id_value, variations in articles.items():

            article_obj = Article(article_number=article_id_value)

            article_fields = {field_name: all_article_catalog_fields[field_name][article_id_value] for field_name in article_fields_name_list}

            article_obj.set_fields(article_fields)

            for variation in variations:
                #remove common fields
                for common_field in all_article_catalog_fields:
                    variation.pop(common_field)

                article_obj.add_variation(variation)

            catalog.add_articles(article_obj)

        return catalog

