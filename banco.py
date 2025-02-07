datosusuarios = [{'Id':0, 
    'Nombre':'Roman',
    'Contrasena':'Hola',
    'cedulaIdentidad': 17789264,
    'Saldo': 1000.00, 
    'Estado':'Guarico'},
    {'Id':1, 
    'Nombre':'Carmen',
    'Contrasena':'Hola1',
    'cedulaIdentidad': 17253519,
    'Saldo': 5000.00, 
    'Estado':'Aragua'}]

def depositar(usuario,montoDepositar):
    montoSaldo = float(usuario['Saldo'])
    total = montoDepositar+montoSaldo
    usuario['Saldo'] = total
    print(f'su saldo quedo en: {usuario['Saldo']}')

def retirar():
    montoSaldo = float(usuario['Saldo'])
    total = montoSaldo - montoRetirar
    if total <= 0:
        print('fondos insuficientes')
    else:
        usuario['Saldo'] = total
        print(f'su saldo quedo en: {usuario['Saldo']}')

def saldo(usuario):
    print(f'Su saldo es {usuario['Saldo']}')

cedula = int(input('Por favor coloque la cedula de identidad\r\n'))
contrasena = input('Por favor coloque la contrasena\r\n')

for usuario in datosusuarios:
    if usuario['cedulaIdentidad'] == cedula and usuario['Contrasena'] == contrasena:
        opcion = input(f'hola, {usuario['Nombre']} buscar la forma de buscarlo\r\n¿Que quieres hacer?\r\n1-Ver Saldo\r\n2-Depositar\r\n3-Retirar\r\n')
        if opcion == '1':
            saldo(usuario)
            break
        elif opcion == '2':
            montoDepositar = float(input('Escriba el monto a depositar(el decimal es con punto):'))
            depositar(usuario,montoDepositar)
            break
        elif opcion == '3':
            montoRetirar = float(input('Escriba el monto a retirar(el decimal es con punto):'))
            retirar(usuario,montoRetirar)
            break
        else:
            print('no eligio un parametro permitido, vuelva a loguease XD')
            break