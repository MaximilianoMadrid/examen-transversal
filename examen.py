import random
import csv
import math

trabajadores=[
    {"nombre:", "Juan Perez"},
    {"nombre:", "Maria Garcia"},
    {"nombre:", "Carlos Lopez"},
    {"nombre:", "Ana Martinez"},
    {"nombre:", "Pedro Rodriguez"},
    {"nombre:", "Laura Hernandez"},
    {"nombre:", "Miguel Sanchez"},
    {"nombre:", "Isabel Gomez"},
    {"nombre:", "Francisco Diaz"},
    {"nombre:", "Elena Fernandez"},
]
sueldos=[]

def asignar_sueldos():
    global sueldos
    sueldos=[random.randint{300000, 2500000}for _ in range(10)]
    print("sueldos asignados aleatoriamente")
    
def clasificar_sueldos():
    print("Sueldo menor a 1.000.000: ", {trabajadores['nombre']} len{s for s in sueldos if s < 1000000})
    for trabajadores in zip(trabajadores):
        if sueldos < 1000000:
            print (f"nombre del trabajador: trabajador{trabajadores} sueldos: ${sueldos}")
    
    
    print("sueldo entre 1.000.000 y 1.800.000: ", {trabajadores['nombre']} len{s for s in sueldos if <=1000000 s <= 1800000})
    for trabajadores in zip(trabajadores):
        if  sueldos <= 1000000 and <= 2000000:
            print (f"nombre del trabajador: trabajador{trabajadores} sueldos: ${sueldos}")
    
    
    print("Sueldo mator a 1.800.000: ", {trabajadores['nombre']} len{s for s in sueldos if s > 1800000})
    for trabajadores in zip(trabajadores):
        if sueldos > 1800000:
            print (f"nombre del trabajador: trabajador{trabajadores} sueldos: ${sueldos}")
    
        
        
        
def ver_estadisticas():
    sueldo_maximo= sueldos(max)
    sueldo_minimo= sueldos(min)
    sueldo_promedio=(sueldo_maximo)/ len(sueldo_minimo)
    media_geometrica=
    
    print(f" el sueldo maximo es: $"[sueldo_maximo])
    print(f" el sueldo minimo es: $"[sueldo_minimo])
    print(f"el promedio de los sueldos es: $"[sueldo_promedio])
    print(f"la media geometrica es: $"[media_geometrica:])
    print(f"El total es de:")
    
def reporte_de_sueldo():
    
    descuento_salud= sueldos*0.07
    descuento_afp= sueldos*0.12
    sueldo_liquido=(sueldos-descuento_salud-descuento_afp)
    
    print("\n nombre empleado {nombre} sueldo{sueldo} descuento salud {descuento_salud} descuento AFP {descuento_afp} sueldo liquido {sueldo_liquido}")
    
    
    
    
    
def saliendo_del_programa():
    print("programa finalizado.")
    print("creado por Maximiliano Madrid")
    print("RUT: 12.202.022.2")
    
def menu():
    while True:
     print("1-Asignar sueldos")
     print("2-Clasificar sueldos")
     print("3-Ver estadisticas")
     print("4-reporte de sueldo")
     print("5-saliendo del programa")
     op=int(input("Escoja una opcion:"))
    
     if op==1:
        asignar_sueldos()
     if op==2:
        clasificar_sueldos()
     if op ==3:
        ver_estadisticas()
     if op ==4:
        reporte_de_sueldo()
     if op==5:
        saliendo_del_programa()
        break
     
     else:
         print("Opcion no valida")
      
if __name__: "menu"
menu()      