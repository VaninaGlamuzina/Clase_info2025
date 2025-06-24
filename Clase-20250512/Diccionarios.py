 #Almacena     clave     valor
# diccionario = {'Info': 3424010203}

# Creacion de un diccionario

# diccionario = {'Pais':'Argentina',
#                'Provincia': 'Chaco',
#                'Ciudad': 'Resistencia',
#                'cp': 3500}

# print(diccionario)

## Accediendo a un valor Usando su clave 

# diccionario = {'Pais':'Argentina',
#                'Provincia': 'Chaco',
#                'Ciudad': 'Resistencia',
#                'cp': 3500}

# print(diccionario['cp'])

## Agregando un par Clave Valor 

# diccionario = {'Pais':'Argentina',
#                'Provincia': 'Chaco',
#                'Ciudad': 'Resistencia',
#                'cp': 3500}

# print(diccionario)

# diccionario['Departamento'] = 'San Fernando'

# print(diccionario)

## Para modificar un Valor 

# curso = {'Nombre': 'Info',
#          'Etapa': 1}

# print(curso)
# curso['Etapa'] = 2
# print(curso)

## La forma en la que podemos recorrer los diccionarios usando condicionales 

# curso = {'Nombre': 'Info',
#          'Etapa': 1}

# if 'Nombre' in curso:
#     print('La clave Nombre se encuentra en el diccionario')
# else:
#      print('La clave Nombre NO se encuentra en el diccionario')   

## La forma en la que podemos recorrer los diccionarios usando bucles

# curso = {'Nombre': 'Info',
#           'Etapa': 1}

# for clave, valor in curso.items():
#     print(f'Clave: {clave}. Valor: {valor}')

## Para obtener claves y valores seguiremos de la siguiente frma 

# curso = {'Nombre': 'Info',
#           'Etapa': 2}

# Claves = list(curso.keys())
# Valores = list(curso.values())

# print(f'Las claves del diccionario son: {Claves}, y los valores son: {Valores}.')