from file_manager import FileManager


class Mapper():
    """mapping a dictionary to mapping csv file fieldss.
    creates destination fields and removes source fields."""

    MAPPER_FILE_ADDRESS = 'mappings.csv' # can make it dynamic

    MAPPING = []

    def __init__(self) -> None:
        self.mapper_file = FileManager(self.MAPPER_FILE_ADDRESS)
        self.generate_mapping_dict()

    def generate_mapping_dict(self) -> None:
        """generating a mapping dictionary with destination and source key, values."""

        while mappig := self.mapper_file.get_row_data():
            self.MAPPING.append(mappig)

    def map(self, data: dict) -> dict | None:
        """mapping a dictionary to desired values. 
        adds new destination fields and removes source fields."""

        if not data:
            return None

        for mapping in self.MAPPING:
            source_types = mapping['source_type'].split('|')
            sources = mapping['source'].split('|')
            for source_type, source in zip(source_types, sources):
                if data.get(source_type) and source == data[source_type]:
                    data.pop(source_type)
                    data[mapping['destination_type']] = mapping['destination']

        return data

