
# Bool contiene los valores de True y False
# Los tipos numericos es false para el 0 y true para los demas valores
valor = 0
resultado = bool(valor)
print(f'El valor: {valor}, Resultado: {resultado} ')

valor = -1
resultado = bool(valor)
print(f'El valor: {valor}, Resultado: {resultado} ')

# Tipo String -> False '', True para los demas valores
valor = ''
resultado = bool(valor)
print(f'El valor: {valor}, Resultado: {resultado} ')

valor = 'hola'
resultado = bool(valor)
print(f'El valor: {valor}, Resultado: {resultado} ')

# Tipo colecciones False -> colecciones vacias
# Tipo colecciones True -> demas valores
# Lista
valor = []
resultado = bool(valor)
print(f'El valor de una lista vacia: {valor}, Resultado: {resultado} ')

valor = [2, 3, 'hola']
resultado = bool(valor)
print(f'El valor de una lista con elemento: {valor}, Resultado: {resultado} ')

# Tupla
valor = ()
resultado = bool(valor)
print(f'El valor de una tupla vacia: {valor}, Resultado: {resultado} ')

valor = ('hola', 2)
resultado = bool(valor)
print(f'El valor de una tupla con elemento: {valor}, Resultado: {resultado} ')

# Diccionario

valor = {}
resultado = bool(valor)
print(f'El valor de un diccionario vacio: {valor}, Resultado: {resultado} ')

valor = {'nombre': 'Nicolas', 'apellido': 'Guala'}
resultado = bool(valor)
print(f'El valor de un diccionario con elementos: {valor}, Resultado: {resultado} ')

# Sentencias de control con booleanos
if '':
    print('Regresa verdadero')
else:
    print('Regresa falso')

if 'hola':
    print('Regresa verdadero')
else:
    print('Regresa falso')

# Ciclos
variable = 0
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')