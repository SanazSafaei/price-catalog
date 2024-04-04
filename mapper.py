from file_manager import FileManager


class Mapper():
    """mapping a dictionary to mapping csv file fieldss.
    creates destination fields and removes source fields."""

    mapping = []

    def __init__(self, mapping_file_address: str) -> None:
        self.mapper_file = FileManager(mapping_file_address)
        self.generate_mapping_dict()

    def generate_mapping_dict(self) -> None:
        """generating a mapping dictionary with destination and source key, values."""

        while mappig := self.mapper_file.get_row_data():
            if not mappig['source'] and not mappig['destination']:
                source_types = mappig['source_type'].split('|')
                destination_type = '_'.join(source_types)

                mappig['destination_type'] = destination_type
            self.mapping.append(mappig)

    def map(self, data: dict) -> dict[str, str] | None:
        """mapping a dictionary to desired values. 
        adds new destination fields and removes source fields."""

        if not data:
            return None

        for mapping in self.mapping:
            source_types = mapping['source_type'].split('|')
            sources = mapping['source'].split('|')
            match = True
            for source_type, source in zip(source_types, sources):

                if not mapping['source'] and not mapping['destination']:
                    continue

                if not data.get(source_type) or source != data[source_type]:
                    match = False
                    break

            if match:
                if not mapping['source'] and not mapping['destination']:
                    destination_value = ''
                    skip = False
                    for source_type in source_types:
                        if destination_value:
                            destination_value = f"{destination_value} {data[source_type]}"
                        elif data.get(source_type):
                            destination_value = data[source_type]
                        else:
                            skip = True
                            break
                    if not skip:
                        data[mapping['destination_type']] = destination_value
                else:
                    data[mapping['destination_type']] = mapping['destination']
        return data

