"""
Дано два словаря
A = {'key': 1}
B = {'key1: 2}
Необходимо написать код который будет их объединять
C = {'key': 1, 'key1': 2}
Но нужно так-же учитывать коллизии,
например ситуация когда у нас два одинаковых ключа и
чтобы не потерять значения нужно записать в один ключ список в котором будут находится значения
Например:
A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}
C = {'key': [1, 'Hello'], 'key2': True}
Записать результат в файл result.json в формате JSON.
"""

import json

A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}
C = {}

for d in A, B:
    for k, v in d.items():
        C.setdefault(k, []).append(v)

json_C = json.dumps(C)
print(json_C)

with open("data.json", "w") as f:
    f.write(json_C)
