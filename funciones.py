### for x in fila
###     print("fila : ",matriz[x],end=" ")
###     for y in columna
###         print(matriz[x][y],end=" ")
###         print(" ")

from os import system
from numpy import zeros
habitacion = zeros((2,5),int)
valor_dia = 15000

lista_rut_dueno = []
lista_nombre_dueno = []
lista_id = []
lista_nombre_mascota = []
lista_dias = []
lista_habitaciones = []
lista_totales = []
id_cont=0
def lp():
    system('cls')

def grabar():
    lp()
    while True:
            try:
                rut_dueno = int(input("INGRESE RUT DEL DUEÑO SIN DIGITO VERIFICADOR, NI PUNTOS NI GUIONES\n\t>>> "))
                if rut_dueno>=1000000 and rut_dueno<=99999999:
                    lista_rut_dueno.append(rut_dueno)
                    break
                else:
                    print("ERROR! DEBES INGRESAR UN RUT VALIDO!")
            except:
                lp()
                print("ERROR! DEBES INGRESAR UN NUMERO DE RUT SIN DIGITO VERIFICADOR NI PUNTOS NI GUIONES!")
            
    
    while True:
        try:
            nombre_dueno = str(input("INGRESE NOMBRE DEL DUEÑO\n\t>>> "))
            if len(nombre_dueno)>=3 and len(nombre_dueno)<=99:
                lista_nombre_dueno.append(nombre_dueno)
                break
            else:
                lp()
                print("ERROR! DEBES INGRESAR UN NOMBRE VALIDO!")
        except:
            print("ERROR! DEBES ESCRIBIR UN NOMBRE VALIDO!")
    
        

    while True:
        try:
            nombre_mascota = str(input("INGRESE NOMBRE DE LA MASCOTA\n\t>>> "))
            if len(nombre_mascota)>=3 and len(nombre_mascota)<=99:
                lista_nombre_mascota.append(nombre_mascota)
                break
            else:
                lp()
                print("ERROR! DEBES INGRESAR UN NOMBRE VALIDO!")
        except:
            print("ERROR! DEBES ESCRIBIR UN NOMBRE VALIDO!")
    
    while True:
        try:
            dias = int(input("INGRESE CANTIDAD DE DIAS DE PERMANENCIA\n\t>>> "))
            if dias>=1:
                lista_dias.append(dias)
                total = dias*15000
                lista_totales.append(total)
                break
        except:
            print("ERROR! DEBES INGRESAR UNA CANTIDAD DE DÍAS VALIDOS!")
            
            
    lp()
    print("DISPONIBILIDAD:")
    for x in range(2):
        print("piso ",x+1,": ",end=" ")
        for y in range(5):
            print(habitacion[x][y],end=" ")
        print(" ")
        
    print(" ")
    print("PARA EL NUMERO DE LAS\nHABITACIONES CONSIDERE\nESTE ORDEN:")
    print("piso  1 :  1 2 3 4 5")
    print("piso  2 :  6 7 8 9 10")
    print(" ")
    while True:
        try:
            asignacion = int(input("INGRESE UNA HABITACIÓN DESEADA\n\t>>> "))
        except:
            print("ERROR! DEBES INGRESAR UNA HABITACIÓN VALIDA!")
        if asignacion>0 and asignacion<11:
                if asignacion>=1 and asignacion<=5:
                    if habitacion[0][asignacion] != 0:
                        print("LA HABITACIÓN YA ESTÁ OCUPADA!")
                    else:
                        habitacion[0][asignacion] = 1
                        break
                elif asignacion>=6 and asignacion<=10:
                    if habitacion[1][asignacion-5] != 0:
                        print("LA HABITACIÓN YA ESTÁ OCUPADA!")
                    else:
                        habitacion[1][asignacion-5] = 1
                        break
        else:
            print("ERROR! DEBES INGRESAR UN NUMERO DE HABITACION VALIDA ENTRE 1 Y 1O!")    
    
        
        
def buscar():
    lp()
    while True:
        value = None
        try:
            busqueda=int(input("INGRESE RUT DEL DUEÑO\n\t>>> "))
        except:
            print("ERROR! DEBES INGRESAR UN NUMERO DE RUT VALIDO SIN DIGITO VERIFICADOR NI PUNTOS NI GUIONES!")
        if busqueda>=1000000 and busqueda<=99999999:
            break
        else:
            print("ERROR! DEBES INGRESAR UN RUT VALIDO!")
    for x in range(len(lista_rut_dueno)):
        if x == busqueda:
            value = x 
            break
        else:
            pass
    if value == None:
        print("NO SE PUDO UBICAR LA HABITACIÓN ASIGNADA A LA MASCOTA DEL DUEÑO DEL RUT ",busqueda)
    else:
        print("LA HABITACIÓN DE LA MASCOTA ASIGNADA AL RUT DE DUEÑO ",busqueda," ES LA HABITACIÓN NÚMERO ",lista_habitaciones[value])        
        
def retirarse():
    lp()
    while True:
        value = None
        try:
            busqueda=int(input("INGRESE RUT DEL DUEÑO"))
        except:
            print("ERROR! DEBES INGRESAR UN NUMERO DE RUT VALIDO SIN DIGITO VERIFICADOR NI PUNTOS NI GUIONES!")
        if busqueda>=1000000 and busqueda<=99999999:
            break
        else:
            print("ERROR! DEBES INGRESAR UN RUT VALIDO!")
    for x in range(len(lista_rut_dueno)):
        if x == busqueda:
            value = x 
            break
        else:
            pass
    if value == None:
        print("NO SE PUDO UBICAR ASIGNADA A LA MASCOTA DEL DUEÑO CON RUT ",busqueda)
    else:
        print("EL TOTAL A PAGAR ES DE ",lista_totales[value]," PESOS")        
    
    

def salir():
    print("GRACIAS POR VISITARNOS!")

def main():
    txt="""
MENU

1. GRABAR
2. BUSCAR
3. RETIRARSE
4. SALIR

""" 
    while True:
        lp()
        print(txt)
        opcion= int(input("INGRESE LA OPCIÓN QUE DESEA\n\t>>> "))
        if opcion == 1:
                grabar()
        elif opcion == 2:
                buscar()
        elif opcion == 3:
                retirarse()
        elif opcion == 4:
                salir()
                break
        else:
            print("ERROR! DEBES INGRESAR UNA OPCIÓN VALIDA!")