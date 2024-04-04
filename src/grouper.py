

class Grouper:
    """"classify list of dictionaries to their common {field: values}"""

    def __init__(self, data_list: list) -> None:
        self.data_list = data_list

    def find_common_fields_with_values(self) -> list[dict[str,str]]:
        """"classify a list of dictionary to their common {field: values}"""

        try:
            common_field_value = {}

            for item in self.data_list:

                if not common_field_value:
                    common_field_value = item.copy()

                else:
                    common_field_value_temp = common_field_value.copy()
                    for filed, value in common_field_value_temp.items():
                        if item.get(filed) != value:
                            common_field_value.pop(filed)

            return common_field_value

        except Exception:
            raise ValueError('data is not valid.')


    def group_by_specific_field(self, article_id_name: str) -> tuple[dict[str, list[dict[str, str]]], dict[str, dict[str, str]]]:
        """"classify a list of dictionary with a id and
        find objects common {article_id_name: values}"""
        try:
            grouped_items = {}
            common_field_value = {}
            deleted_fields = []

            for item in self.data_list:

                if item.get(article_id_name) and item.get(article_id_name) in grouped_items:
                    grouped_items[item[article_id_name]].append(item)

                    common_field_value_copy = common_field_value.copy()
                    for item_field, value_lists in common_field_value_copy.items():

                        if ((value_lists.get(item[article_id_name]) and 
                            item[item_field] != value_lists[item[article_id_name]]) or
                            not value_lists.get(item[article_id_name])) :

                            deleted_fields.append(item_field)
                            common_field_value.pop(item_field)

                else:
                    grouped_items[item[article_id_name]] = [item]
                    for item_field in item:
                        if item_field not in deleted_fields:

                            if common_field_value.get(item_field):
                                common_field_value.get(item_field).update({item[article_id_name]: item[item_field]})
                            else:
                                val = {item[article_id_name]: item[item_field]}
                                common_field_value[item_field] = val

            return grouped_items, common_field_value
        
        except Exception:
            raise ValueError('data is not valid.')
