from os  import system
from time import sleep
contador = 0
agenda = {}

def Imprimir_Menu():
    system("cls")
    print( '''
+++++++++++++++++++++++++++++++++++++++++++++++

Opciones de menu
-----------------------------------------------
1. crer un contacto
2. modificar contacto
3. eliminar contacto
4. mostrar agenda
5. buscar contacto
0. salir

+++++++++++++++++++++++++++++++++++++++++++++++
''')

def buscar_contact():
    
    print( """
    +++++++++++++++++++++++++++++++++++++++++++++++

    Menu de busqueda
    -----------------------------------------------
    1 - Nombre
    2 - Telefono
    3 - Empresa


    +++++++++++++++++++++++++++++++++++++++++++++++
    """)
    busqueda_menu= input('Opcion')

    if busqueda_menu == '1':
        nombre = input("1 - Nombre: ")
        if nombre in agenda:
            print (agenda[nombre])
        else :
            print("Contacto no existente")
    if busqueda_menu == '2':
        telefono = input("2 - Telefono: ")
        
        if nombre.telefono in agenda:
            print(agenda[nombre][telefono])
        else :
            print("telefono no existente")
            
    if busqueda_menu == '3':
        empre= input("3 - Empresa")
        if nombre.empre in agenda:
            print(agenda[nombre][empre])
        else :  
            print("empresa no existente")
    sleep(3)

def Crear_contacto():
    nombre = input('Ingrese un nombre: ')
    if nombre in agenda.keys():
        print('esta nombre ya existente: ')
    else:
        dtelefono = input('Ingrese telefono: ')
        empresa = input('Ingrese empresa: ')
        agenda[nombre]= {}
        agenda[nombre]["telefono"]  =dtelefono

        agenda[nombre]["empresa"] = empresa
        print('ingresado correctamente!!!')
    sleep(3)
        
            
def Modificar_contacto():
    
    nombre = input('Ingrese un nombre: ')
    if nombre in agenda.keys():
        dtelefono = input('Ingrese un nueva telefono: ')
        empresa = input(' Ingrese una empresa: ')
        agenda[nombre]["telefono"] = dtelefono
        agenda[nombre]["Empresa"] =empresa
    else:
        print('esta categoria no existente')
    sleep(3)

def eliminar_contacto():
    nombre = input('Ingrese un nombre: ')
    if nombre in agenda.keys():
        agenda.pop(nombre)
          
    else:
        print('esta categoria no existente')
    sleep(3)
        
        
def mostrar_agenda():
    
    print(agenda)
    sleep(3)


while True:
    Imprimir_Menu()
    op = int(input("Opcion: "))
    
    if op == 1: Crear_contacto()
    elif op == 2: Modificar_contacto()
    elif op == 3: eliminar_contacto()
    elif op == 4: mostrar_agenda()
    elif op == 5: buscar_contact()
    elif op == 0: break
    else: print(' no corresponde a ninguna opcion ')
    
    
    
             
    