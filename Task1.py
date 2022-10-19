"""
1.Дан список словарей, необходимо записать их в файл с помощью модуля pickle.
В каждом из словарей одинаковый набор ключей, а все значения представлены в виде строк
"""

import pickle

clients = [
    {
        'user': 'Olga',
        'mail': 'olga@gmail.com',
        'residency': 'Ukraine'
    },
    {
        'user': 'Oleg',
        'mail': 'oleg@ukr.net',
        'residency': 'Cyprus'
    },
    {
        'user': 'Andriy',
        'mail': 'andriy@ukr.net',
        'residency': 'Ukraine'
    },
]

with open("data.txt", "wb") as f:
    pickle.dump(clients, f)
