def swap(items):
    if len(items) >= 2:
        items[0], items[-1] = items[-1], items[0]
    return items 