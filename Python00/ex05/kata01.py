import sys

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for clave, valor in kata.items():
    print(clave + ': ' + valor)