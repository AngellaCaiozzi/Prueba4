import FuncConciertoTrap as fc

opcion = ''
diccComprador = {}


while opcion != '4':
    opcion = fc.MenuConcierto()
    if opcion == '4':
        print('Programa Terminado.')
    elif opcion == '1':
        print('Comprar Entrada')
        diccComprador = fc.ComprarEntrada(diccComprador)  
        print(diccComprador)  
    elif opcion == '2':
        print('Consultar Comprador.')
        diccComprador = fc.ConsultarComprador(diccComprador)
    elif opcion == '3':
        print('Cancelar Compra') 
        diccComprador = fc.cancelarCompra(diccComprador)  
    else:
        print('Error. Opción no existe. ')     
