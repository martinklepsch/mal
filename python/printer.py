import reader, numbers

def pr_str(data):
    if reader._symbol_Q(data):
        return str(data)
    elif isinstance(data, numbers.Number):
        return str(data)
    elif isinstance(data, list):
        list_items = []
        for d in data:
            list_items.append(pr_str(d))
        print list_items
        return "(" + " ".join(list_items) + ")"
