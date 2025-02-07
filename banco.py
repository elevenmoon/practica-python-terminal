datosusuarios = [{'Id':0, 
    'Nombre':'Roman',
    'cedulaIdentidad': 17789264,
    'Saldo': 1000.00, 
    'Estado':'Guarico'},
    {'Id':1, 
    'Nombre':'Carmen',
    'cedulaIdentidad': 17253519,
    'saldo': 5000.00, 
    'Estado':'Aragua'}]

usuarios = [17789264,17253519]

contrasenasusuarios = [{'Id':0, 
    'Contrasena':'Hola'},
    {'Id':1, 
    'Contrasena':'Hola1'}]

tamano = len(datosusuarios)
print(tamano)

usuario = int(input('Por favor coloque la cedula de identidad\r\n'))
contrasena = input('Por favor coloque la contrasena\r\n')

valorusuario = usuario in usuarios
for contrasena in contrasenasusuarios:
    print('hola')

print(valorusuario)
print(valorcontresena)

if usuario in usuarios and contrasena in contrasenasusuarios:
    opcion = input(f'hola, ${usuario} buscar la forma de buscarlo\r\n¿Que quieres hacer?\r\n1-Ver Saldo\r\n2-Depositar\r\n3-Retirar')
    if opcion == '1':
        print(f'Su saldo es ')
    elif opcion == '2':
        montoDepositar = float(input('Escriba el monto a depositar:'))
    elif opcion == '3':
        montoRetirar = float(input('Escriba el monto a depositar:'))
    else:
        print('no eligio un parametro permitido, vuelva a loguease XD')
else:
    print('el usuario no es permitido')

def login():
    print('revisar el login del usuario')

def depositar():
    print('aqui se va a sumar dinero')

def retirar():
    print('aqui se va retirar dinero')

def saldo():
    #primero a hacer es este
    print('aqui ser va a revisar el saldo ')