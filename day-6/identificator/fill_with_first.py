def fill_with_first(items):
    if items:
        first_item = items[0]
        items[:] = [first_item] * len(items)