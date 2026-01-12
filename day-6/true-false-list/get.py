def get(items,index, default=None):
    if -len (items) <= index < len(items):
        return items[index]
    else:
        return default