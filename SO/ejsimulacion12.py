import os

# Consideraciones:
# * el 10% del SO esta al comienzo de la memoria
# * NO puede haber una sola particion 
# * la memoria tiene 2 campos: estado (T o F) y contenido 
# * No hay limitaciones para el tamaño de la memoria

#-----------------FUNCION PARA CARGAR LOS TAMAÑOS DE LAS PARTICIONES------------

def cargarTamPart(cantParticiones):
	j = 0 
	tamPart = [None] * cantParticiones
	while None in tamPart:
		print('Particion numero:', j+1)
		aux = int(input('Ingresar el tamaño de la particion: '))
		while aux <= 0 or aux in tamPart or aux>=tam:
			print('ERROR, tamaño no permitido')
			aux = int(input('Ingresar otro tamaño de la particion: '))
		tamPart[j] = aux
		j+=1
	return tamPart

#------------------------------------INICIO--------------------------------------

os.system('cls')
tam = int(input('Ingresar el tamaño de Memoria: '))
# limite superior de tamaño ? 
while tam <= 0: 
	print('Tamaño de memoria invalido, intente de nuevo')
	tam = int(input('Ingresar tamaño de Memoria: '))
print('\nTamaño de la memoria: ', tam)

#-------------------INICIALIZO LA MEMORIA---------------------

memoria = [x[:] for x in [[0] * 2] * tam]
for i in range(tam):
	memoria[i][0] = True
	memoria[i][1] = 'libre' 
#--------------------------ESPACIO DE SO----------------------

espacioSo = int(tam * 0.1)
print('Espacio ocupado por el SO:',espacioSo)
for i in range(espacioSo):
	memoria[i][0] = False
	memoria[i][1] = 'SO'
disp = tam - espacioSo
print('Espacio disponible:', disp)

#------------------CUANTAS PARTICIONES?--------------------------

cp = int(input('\nIngresar la cantidad de Particiones: '))

while cp > disp or cp <= 1:
	print('ERROR La cantidad de particiones debe ser menor a', disp,'y deben haber al menos 2 particiones')
	cp = int(input('Ingresar la cantidad de Particiones: '))
os.system('cls')
print('Numero de particiones:', cp)

#----------------CARGA DE TAMAÑOS DE PARTICIONES------------------

arregloTamPart =  cargarTamPart(cp)

# nos aseguramos que las particiones entren
while sum(arregloTamPart) > (disp):
	# poner un clear screen aca 
	print('ERROR: el espacio de particiones supera el tamaño de la Memoria\nIntente de nuevo')
	input('')
	os.system('cls')
	print('Numero de particiones:', cp)
	arregloTamPart =  cargarTamPart(cp)

#--------------------------TABLA DE PARTICIONES---------------------------------------- 

tablaParticiones = [p[:] for p in [[0] * 6] * cp ]

# usamos tablaAux para la asignacion de particiones a procesos
tablaAux = [x[:] for x in [[0] * 2] * cp]

# 0- Id de partición, 
# 1- dirección de comienzo de partición, 
# 2- estado de la partición, 
# 			AGREGAR:
# 3- tamaño de la partición, 
# 4- id de proceso asignado a la partición, 
# 5- fragmentación interna

inicio = espacioSo
for k in range(cp):

	for i in range(inicio, inicio + arregloTamPart[k]):
		memoria[i][0] = True 

	tablaParticiones[k][0], tablaAux[k][0] = k, k				
	tablaParticiones[k][1] = inicio 	
	tablaParticiones[k][2] = True		
	tablaParticiones[k][3], tablaAux[k][1] = arregloTamPart[k], arregloTamPart[k]

	inicio = inicio + arregloTamPart[k]		

# os.system('cls')
print('PRESS ENTER')
input('')

#-------------------------CARGA DE PROCESOS-------------------------------

os.system('cls')
print('CARGA DE PROCESOS')

# muestro la tabla para vea cuantas particiones hay y sus tamaños
# print('Tabla de Particiones: ')
# c = len(tablaParticiones)
# print('idParticion, inicio, estado, tamaño, idProceso, fragmentación interna')
# for j in range(c):
# 	print(str(j),'_\t',tablaParticiones[j])

# ordeno tablaAux en funcion del campo tamaño, de mayor a menor
tablaAux.sort( key = lambda x:x[1], reverse = True)

# para hacer el control de no ingresar un proceso que 
# no entre en la particion mas grande
tamMax = tablaAux[0][1]

cantPrCarg = 0 

# "El programa debe permitir ingresar procesos mientras haya memoria libre para asignar"
while cantPrCarg < cp:

	print('Cantidad de procesos cargados:', cantPrCarg)
	print('\nProceso', cantPrCarg + 1)

	tamPr = int(input('Ingresa tamaño: '))
	while tamPr <= 0 or tamPr > tamMax:
		print('ERROR tamaño de proceso invalido, intente de nuevo')
		tamPr = int(input('Ingresa tamaño: '))

	menor = 999999
	pos = 0
	exito = False

	# cp es igual a la cantidad de elementos en la tabla de particiones
	for i in range(cp):
		# verifico si la particion esta disponible
		if tablaParticiones[i][2] == True:
			# busco el dif mas pequeño posible
			dif = tablaParticiones[i][3] - tamPr
			# pregunto por la menor dif hasta el momento
			if dif >=0 and dif < menor:
				menor = dif 
				# pos el indice de la TP donde esta la particion
				# donde tengo que guardar el proceso
				pos = i 
				# encontre al menos una particion donde puedo
				# guardar el proceso
				exito = True

	if exito:
		print('El proceso entra en la particion', tablaParticiones[pos][0])	

		# --------CARGA EN MEMORIA---------
		# nomPr es el contenido que ponemos en memoria 
		nomPr = 'p' + str(cantPrCarg)
		# para hacer la carga en memoria
		desde = tablaParticiones[pos][1]
		hasta = desde + tamPr
		# cargo el proceso en memoria
		for j in range(desde, hasta):
			memoria[j][1] = nomPr

		# ---------ACTUALIZACION TP---------------
		# pasa a estar ocupada la particion
		tablaParticiones[pos][2] = False
		# en id de proceso ponemos el numero de orden de los procesos que van siendo cargados
		tablaParticiones[pos][4] = cantPrCarg
		# fragmentacion interna 
		tablaParticiones[pos][5] = tablaParticiones[pos][3] - tamPr
		print('Tabla de particiones: ')
		for i in range(cp):
			print(tablaParticiones[i])

		cantPrCarg += 1 

	else:
		print('ERROR No se encontro particion para el proceso')









