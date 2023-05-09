
def items_to(list, prop, value):
    # each object is a dict
    return [item for item in list if item[prop] == value]
