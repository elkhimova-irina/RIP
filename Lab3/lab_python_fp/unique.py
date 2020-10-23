class Unique(object):
    def __init__(self, items, **kwargs):
        self.unique_items = []
        self.items = iter(items)
        if 'ignore_case' not in kwargs:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        # Нужно реализовать __next__

        while True:
            item = self.items.__next__()
            compare_item = None
            if self.ignore_case and type(item) is str:
                compare_item = item.lower()
            else:
                compare_item = item
            if compare_item not in self.unique_items:
                self.unique_items.append(compare_item)
                return item

    def __iter__(self):
        return self

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
print(list(Unique(data)))
