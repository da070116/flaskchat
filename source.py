def get_max_from_dict(elements, max_key):
    try:
        max_elem = elements[0]
        max_value = max_elem[max_key]

        for item in elements[1:]:
            if max_value < item[max_key]:
                max_value = item[max_key]
                max_elem = item
    except IndexError:
        print("Empty dictionary given")
        max_elem = None
    except TypeError:
        print("Can't convert value")
        max_elem = None
    return max_elem


def filter_dict(elements, filter_key, edge_value):
    filtered_list = []
    for item in elements:
        try:
            if item[filter_key] >= edge_value:
                filtered_list.append(item)
        except TypeError:
            filtered_list = []
    return filtered_list
