lst = [
    {'name': '贵', 'price': 10, 'count': 1},
    {'name': '贵', 'price': 10, 'count': 1},
    {'name': '有点贵', 'price': 100, 'count': 1},
    {'name': '贵', 'price': 10, 'count': 1},
    {'name': '有点贵', 'price': 100, 'count': 1},
    {'name': '好贵', 'price': 1000, 'count': 1}
]


for i in lst[::]:
    if i['name'] == '贵':
        lst.remove(i)

print(lst)

