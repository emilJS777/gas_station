# DICT ITEMS
def get_dict_items(obj):
    dict_item = {}

    if not obj:
        return obj

    for key, value in obj.__dict__.items():
        if not key == '_sa_instance_state' and not key == 'password_hash':
            dict_item[key] = value

    return dict_item


# PAGE ITEMS
def get_array_items(array):
    items: list = []

    for item in array:
        items.append(get_dict_items(item))

    return items


# PAGE ITEMS
def get_page_items(page):
    page_items: dict = {'total': page.total,
                        'page': page.page,
                        'pages': page.pages,
                        'per_page': page.per_page,
                        'items': []}

    for item in page.items:
        page_items['items'].append(get_dict_items(item))

    return page_items
