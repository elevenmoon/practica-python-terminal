negocios = [{'Id':0, 
    'Nombre':'NUCLEO',
    'Categoria':'MP', 
    'Estado':'Guarico'},
    {'Id':1, 
    'Nombre':'PVC de mexichem', 
    'Categoria':'MP', 
    'Estado':'Aragua'}]

def buscarNegocioNombre(nombrebuscar):
    for negocio in negocios:
        if negocio['Nombre'] == nombrebuscar:
            print(f'El nombre del negocio es: {negocio['Nombre']}\r\nLa categoria es: {negocio['Categoria']}\r\nEsta en el estado:{negocio['Estado']}')
            break

def buscarNegocioCategoria(categoriabuscar):
    for negocio in negocios:
        if negocio['Categoria'] == categoriabuscar:
            print(f'El nombre del negocio es: {negocio['Nombre']}\r\nLa categoria es: {negocio['Categoria']}\r\nEsta en el estado:{negocio['Estado']}')

def agregarNegocio(nombre,categoria,estado):
    valorid = len(negocios)
    negocios.append({'Id':valorid, 'Nombre':nombre,'Categoria':categoria,'Estado':estado})
    print(negocios)
    #Se debe agregar un valor a la lista



for elem in negocios:      #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
    for k,v in elem.items():        #acedemos a cada llave(k), valor(v) de cada diccionario
        print(k, v)

#Se debe buscar buscar por Nombre y por categoria

opcion = input('Hola,\r\n¿Quieres buscar o agregar un nuevo?\r\nElige una de estas opciones:\r\n1- Buscar por nombre\r\n2- Buscar por categoria\r\n3- Agregar un negocio\r\n')

if opcion == '1':
    nombrebuscar = input('Colocar el nombre a buscar: ')
    buscarNegocioNombre(nombrebuscar)
elif opcion == '2':
    categoriabuscar = input('Colocar la categoria a buscar ')
    buscarNegocioCategoria(categoriabuscar)
elif opcion == '3':
    nombre = input('Colocar el nombre del negocio: \r\n')
    categoria = input('Colocar la categoria del negocio: \r\n')
    estado = input('Colocar el estado de ubicacion del negocio \r\n')
    agregarNegocio(nombre,categoria,estado)
else:
    print('Se equivo de opcion')



