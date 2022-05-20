import json

data = [
    {'name': 'Стул повышенного качества 1',
        'description': 'Не оторваться. ', 'image': '/static/img/product-11.jpg'},
    {'name': 'Стул повышенного качества 2',
        'description': 'Не оторваться. ', 'image': '/static/img/product-21.jpg'},
    {'name': 'Стул повышенного качества 3',
        'description': 'Не оторваться. ', 'image': '/static/img/product-31.jpg'},
]


with open("data.txt", "w") as write_file:
    json.dump(data, write_file)
