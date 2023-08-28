import json
from datetime import datetime


def transform_value(data_type, value):
    """
    Transforms the value based on its data type.
    """
    if isinstance(value, str):
        value = value.strip()

    if data_type == "S":
        try:
            return int(datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ').timestamp())
        except ValueError:

            return value if value else None

    elif data_type == "N":
        try:
            num_value = float(value)
            return int(num_value) if num_value.is_integer() else num_value
        except ValueError:
            return None

    elif data_type == "BOOL":
        true_values = ["1", "t", "T", "TRUE", "true", "True"]
        false_values = ["0", "f", "F", "FALSE", "false", "False"]
        if value in true_values:
            return True
        elif value in false_values:
            return False
        else:
            return None

    elif data_type == "NULL":
        true_values = ["1", "t", "T", "TRUE", "true", "True"]
        if value in true_values:
            return None
        else:
            return "omit_field"

    elif data_type == "L":
        if not isinstance(value, list):
            return None
        transformed_list = []
        for item in value:
            if not isinstance(item, dict) or len(item) != 1:
                continue
            item_type, item_value = list(item.items())[0]
            transformed_item = transform_value(item_type.strip(), item_value)
            if transformed_item != "omit_field" and transformed_item is not None:
                transformed_list.append(transformed_item)
        return transformed_list if transformed_list else None

    elif data_type == "M":
        return transform(value) if value else None

    else:
        return None


def transform(json_data):
    """
    Transforms the given JSON data based on the transformation criteria.
    """
    if not isinstance(json_data, dict):
        return None

    transformed_data = {}
    for key, value in json_data.items():
        sanitized_key = key.strip()
        if not sanitized_key or not isinstance(value, dict) or len(value) != 1:
            continue

        data_type, actual_value = list(value.items())[0]
        transformed_value = transform_value(data_type.strip(), actual_value)

        if transformed_value != "omit_field" and transformed_value is not None:
            transformed_data[sanitized_key] = transformed_value

    return dict(sorted(transformed_data.items()))


input_json = {
    "number_1": {
        "N": "1.50"
    },
    "string_1": {
        "S": "784498 "
    },
    "string_2": {
        "S": "2014-07-16T20:55:46Z"
    },
    "map_1": {
        "M": {
            "bool_1": {
                "BOOL": "truthy"
            },
            "null_1": {
                "NULL ": "true"
            },
            "list_1": {
                "L": [
                    {
                        "S": ""
                    },
                    {
                        "N": "011"
                    },
                    {
                        "N": "5215s"
                    },
                    {
                        "BOOL": "f"
                    },
                    {
                        "NULL": "0"
                    }
                ]
            }
        }
    },
    "list_2": {
        "L": "noop"
    },
    "list_3": {
        "L": [
            "noop"
        ]
    },
    "": {
        "S": "noop"
    }
}


transformed_json = transform(input_json)
print(transformed_json)
