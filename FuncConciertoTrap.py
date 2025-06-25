#Funciones Concierto Trap

#Menu
def MenuConcierto():
    print('~~'*20)
    print('MENÚ')
    print('~~'*20)
    print("""
    1.- Comprar Entrada.
    2.- Consultar Comprador.
    3.- Cancelar Compra.
    4.- Salir.""")
    op = input('Ingrese su opción: ')
    return op 

#Definir codigo de confirmacion
def validar_codigo(CodigoConf):
    tieneMayusculas = any(c.isupper() for c in CodigoConf)
    tieneNro = any(c.isdigit() for c in CodigoConf)
    sinEspacios = ' ' not in CodigoConf
    return len(CodigoConf) >= 6 and tieneMayusculas and tieneNro and sinEspacios

#Comprar entrada: nombre, tipo entrada, código confirmación
def ComprarEntrada(diccComprador):
    while True:
        nombre = input('Ingrese nombre del comprador: ').strip()
        if nombre.replace(' ','').isalpha():
            break
        else:
            print('El nombre solo debe contener letras.')

    while True:
        tipo = input('Ingrese tipo de entrada [G: General / V: Vip]: ').upper()
        if tipo == 'G': 
            break
        elif tipo == 'V':
            break
        else:
            print('Tipo no valido. Intente nuevamente.') 

    while True:
        codigo = input('Ingrese código de verificación: ')
        if validar_codigo(codigo):
            break
        else:
            print('Codigo no valido. Intente otra vez.') 

    diccComprador[nombre] = [tipo, codigo] 
    print('Código validado. ¡Entrada registrada con éxito!')        
    return diccComprador

#Consultar comprador
def ConsultarComprador(diccComprador):
    while True:
        nombre = input('Ingrese nombre del usuario: ').strip()
        if nombre in diccComprador:
            diccComprador[nombre]
            print(f'Tipo de entrada: ',diccComprador[nombre][0] , '|Código: ', diccComprador[nombre][1])
            break
        else:
            print('El comprador no se encuentra en la lista.')                 

#Cancelar compra
def cancelarCompra(diccComprador):
    while True:
        nombre = input('Ingrese nombre del usuario: ').strip()
        if nombre not in diccComprador:
            print('El comprador no se encuentra en la lista.')
        else:
            del diccComprador
            print('¡Compra cancelada!')
            break   
            

