# ## creando un conjunto ## entre {llaves} no tienen indice
# conjunto_1 = {'dato', 123, True}
# print(conjunto_1)

# ## para recorrer un conjunto se puede utilizar un condicional ##

# conjunto = {'Info','Chaco','Info', 123, 123}
# print(conjunto)

# if 'Info' in conjunto:
#     print('El valor indicado se encuentra en el conjunto')
# else:
#     print('El valor indicado NO se encuentra en el conjunto')

#---------------------------------------------------------------------------------------------

# ## recorrer el conjunto asignando una variable ##
# conjunto_2 = {'Info','Chaco','Info', 123, 123}

# valor_buscado = 'Chaco' # variable asignada

# if valor_buscado in conjunto_2:
#     print('El valor',valor_buscado,'se encuentra en el conjunto')
# else:
#     print('El valor', valor_buscado, 'indicado NO se encuentra en el conjunto')

#---------------------------------------------------------------------------------------------

# ## para recorrer el conjunto mediante 'for' ##
# conjunto_3 = {'Info','Chaco','Info', 123, 123}

# for i in conjunto_3:
#     print(i)

#---------------------------------------------------------------------------------------------
# ## operaciones con conjuntos ##

# # únion utilizando | .. no tienen un orden ..
# frutas = {'Manzana', 'Banana', 'Melon'}
# verduras = {'tomate', 'lechuga', 'remolacha'}

# frutas_y_verduras = frutas | verduras

# print(frutas_y_verduras)

# intersección utilizando & ..

# caja_1 = {'remera','pantalon','camisa'}
# caja_2 = {'zapato', 'remera', 'campera'}

# repetidos_en_las_cajas = caja_1 & caja_2

# print(repetidos_en_las_cajas)