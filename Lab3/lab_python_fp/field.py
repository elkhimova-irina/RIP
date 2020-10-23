#!/Users/irinaelkhimova/RIP_labs/Lab3/lab_python_fp/bin/python
# -*- coding: utf-8 -*-



goods = [
    {'title': "Ковер", 'price': 2000, 'color': "green"},
    {'title': "Диван для отдыха", 'price': 5300, 'color': "black"}
]


def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for item in items:
            for arg in args:
                if arg in item:
                    yield item[arg]
    else:
        for item in items:
            new_item = {}
            for arg in args:
                if arg in item:
                    new_item[arg] = item[arg]
            if len(new_item.keys()) > 0:
                yield new_item
print(list(field(goods, 'title', 'price')))
print(list(field(goods, 'title')))
