# ## Creando una tupla ## entre (paréntesis)

# # indice   0      1     2
# tupla = ('dato', 123, True)
# ## Accediendo a un elemento mediante el indice ##
# print(tupla[1])

# ## Si bien son inmutables, se pueden reemplazar todos sus elementos ##
# tupla = ('Informatorio', 'Resistencia-Chaco', 2025)
# print(tupla,'\n')

# tupla = ('practicando', 'Remplazar', 'datos')
# print(tupla)

# ## Las tuplas pueden contener listas[] ##
#indice  0 1 2 3 4 5 6 7 8 9   10  
# tupla = (0,1,2,3,4,5,6,7,8,9,[100,200])
# print(tupla,'\n')
# ## accediendo y modificando una lista dentro de una tupla ##
# tupla[10][1] = 2
# print(tupla,'\n')

# ## eliminar y devolver el último elemento en una lista dentro de una tupla ##
# tupla[10].pop()
# print(tupla,'\n')

# ## agregar un elemento en una lista dentro de una tupla ##
# tupla[10].append(300)
# print(tupla)

# ## convirtiendo una tupla en una lista ##
# lista = list(tupla)
# print(lista)
# ## agregando un elemento a la lista ##
# lista.append(13)
# print(lista) 
# ## covertir tupla en una lista ##
# tupla_new = tuple(lista)
# print(tupla_new)
