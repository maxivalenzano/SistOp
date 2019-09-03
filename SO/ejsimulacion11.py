import os

# Consideraciones:
# * el 10% del SO esta al comienzo de la memoria
# * NO puede haber una sola particion 
# *
#  la memoria tiene 2 campos: estado (T o F) y contenido 

#-----------------FUNCION PARA CARGAR LOS TAMAÑOS DE LAS PARTICIONES------------
def cargarTamPart(cantParticiones):
	j = 0 
	tamPart = [None] * cantParticiones
	while None in tamPart:
		print('Particion numero:', j+1)
		aux = int(input('Ingresar el tamaño de la particion: '))
		while aux <= 0 or aux in tamPart or aux>=tam:
			print('ERROR, tamaño no permitido')
			aux = int(input('Ingresar el tamaño de la particion: '))
		tamPart[j] = aux
		j+=1
	return tamPart

#------------------------------------INICIO--------------------------------------

os.system('cls')
tam = int(input('Ingresar tamaño de Memoria: '))
while tam <= 0: 
	print('Tamaño de memoria invalido, intente de nuevo')
	tam = int(input('Ingresar tamaño de Memoria: '))
print('Tamaño de la memoria: ', tam)

#-------------------INICIALIZO LA MEMORIA---------------------
memoria = [x[:] for x in [[0] * 2] * tam]
for i in range(tam):
	memoria[i][0] = True
	memoria[i][1] = 0
#--------------------------ESPACIO DE SO----------------------
espacioSo = int(tam * 0.1)
print('Espacio ocupado por el SO:',espacioSo)
for i in range(espacioSo):
	memoria[i][0] = False
print('Espacio disponible:', tam - espacioSo)

#------------------CUANTAS PARTICIONES?--------------------------
cp = int(input('Ingresar la cantidad de Particiones: '))
while cp > tam or cp <= 1:
	print('ERROR La cantidad de particiones debe ser menor a',tam,'y deben haber al menos 2 particiones')
	cp = int(input('Ingresar la cantidad de Partiones: '))
os.system('cls')
print('Numero de particiones:', cp)

#----------------CARGA DE TAMAÑOS DE PARTICIONES------------------
arregloTamPart =  cargarTamPart(cp)

#-----------------ENTRAN LAS PARTICIONES?-------------------------
while sum(arregloTamPart) > (tam - espacioSo):
	# poner un clear screen aca 
	print('ERROR: las particiones superar el tamaño de la Memoria\nIntente de nuevo')
	input('')
	os.system('cls')
	print('Numero de particiones:', cp)
	arregloTamPart =  cargarTamPart(cp)

# aca ya sabemos que no hay una sola particion,
# que los tamaños de las particiones son diferentes 
# y que no superan el tamaño de la memoria 

tablaParticiones = [p[:] for p in [[0] * 3] * cp ]

inicio = espacioSo
for k in range(cp):

	for i in range(inicio, inicio+arregloTamPart[k]):
		memoria[i][0] = False #ocupado

	tablaParticiones[k][0] = k
	tablaParticiones[k][1] = inicio
	tablaParticiones[k][2] = False

	inicio = inicio + arregloTamPart[k]

os.system('cls')
print('Tamaño de la memoria:', tam)
print('Espacio ocupado por el SO:', espacioSo)
print('Numero de Particiones:', cp)
print('Espacio ocupado por Particiones:', sum(arregloTamPart))
print('Espacio total Ocupado:', sum(arregloTamPart)+espacioSo)
print('Espacio disponible:', tam - (sum(arregloTamPart)+espacioSo))

print('--- MEMORIA --')
b = len(memoria)
for i in range(b):
	print(str(i),'_\t',memoria[i])
print('\n')

print('--- TABLA DE PARTICIONES ---')
c = len(tablaParticiones)
for j in range(c):
	print(str(j),'_\t',tablaParticiones[j])