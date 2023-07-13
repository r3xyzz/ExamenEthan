'''
La productora de eventos “Creativos.cl”, necesita desarrollar una aplicación que permita controlar la venta de entradas al concierto VIP de “Michael Jam” que se realizará de forma exclusiva sólo para 100 asistentes.
El sistema debe permitir las siguientes operaciones, a través de un menú:
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
Las características de cada operación, se detallan a continuación:
Comprar entradas: El sistema debe solicitar al usuario la cantidad de entradas a comprar. Esta cantidad fluctúa entre 1 a 3.
Una vez ingresada la cantidad validada, el sistema debe desplegar en pantalla las ubicaciones que se encuentran disponibles y las vendidas marcadas con una X.
El usuario debe seleccionar una a una las ubicaciones. Si selecciona una ubicación vendida, se desplegará por pantalla un mensaje que “No está disponible”, teniendo que seleccionar otra.
Los precios de las entradas son los siguientes:
* Platinum, $120.000. (Asientos del 1 al 20).
* Gold, $80.000. (Asientos del 21 al 50).
* Silver, $50.000. (Asientos del 51 al 100.).

Cada asiento debe tener registrado el run de la persona que lo ocupará, por lo tanto, al ser un evento VIP, se solicitará al ingreso la cédula de identidad, verificando de esta forma que la persona se encuentra en la lista de asistentes y un encargado lo dirigirá a la ubicación comprada. El RUN se debe registrar en formato de número, sin guión ni puntos (Ejemplo: 12.345.678-9, debe ser 12345678 sin dígito verificador).
Posteriormente, debe mostrar un mensaje que indique que la operación se ha realizado correctamente.
Mostrar ubicaciones disponibles: El sistema debe desplegar el estado actual de la venta de entradas. Esto se debe desplegar de la misma forma que se muestra en la imagen de la opción de “Compra de Entradas”.
Ver listado de asistentes: El sistema debe mostrar el listado de asistentes por RUN, ordenados de menor a mayor, con la finalidad encontrar fácilmente a una persona asistente.
-Mostrar ganancias totales: El sistema debe calcular el total ganado por concepto de entradas y desplegarse la información, según el siguiente ejemplo (omita los colores):

Tipo Entrada / Cantidad / Total
Platinum $120.000 / 2 / $240.000
Gold $80.000 / 4 / $320.000
Silver $50.000 / 10 / $50.0000 
TOTAL / 16 / $1.060.000

OTRAS CONSIDERACIONES:
 El sistema debe validar las opciones del menú.
 Cada opción del menú, debe ejecutarse a través de funciones.
 La opción Salir, debe mostrar un mensaje de salida del sistema, su nombre, apellido y la fecha actual.
 El sistema debe realizar todas las validaciones necesarias requeridas en el ingreso de datos.
 Los datos ingresados se almacenan en arreglos. (Seleccione el tipo de arreglo, de acuerdo a su criterio).
 Considere listas para alguna de las opciones.
'''


##Asientos_Disponibles = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 ,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ,55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69 , 70, 71, 72, 73 ,74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
#Asientos_Ocupados = []
#
#Precios = {
 #   "Platinunm" : 120000,
 #   "Gold" : 80000,
 #   "Silver" : 1060000
 #}
#
#
#Datos_de_asistente = {}

import datetime

asientos = ['']*100
precios = {'Platinum':120000, 'Gold':80000, 'Silver':50000}
asistentes = {}

def Mostrar_Menu():
    #Bienvenida al evento de Creativos.cl
    print(":::::::::::::::::::::::::")
    print("Bienvenido a Creativos.CL")
    print(":::::::::::::::::::::::::")
    print("1.Comprar Boletos ")
    print("2.Mostrar ubicaciones de asientos disponibles ")
    print("3.Ver lista de asistentes ")
    print("4.Mostrar ganancias Totales ")
    print("5.**SALIR** ")


def compra_de_entradas():
    cantidad = int(input("Ingrese la cantidad de boletos a comprar (1-3): "))
    while cantidad < 1 or cantidad > 3:
        print("Cantidad ivalida. INGRESE NUEVAMENTE")
        cantidad =int(input("Ingrese la cantidad de boletos a comprar (1-3): "))
    
    print("Ubicaciones de asientos disponibles:")
    for e, asiento in enumerate(asientos):
        if asiento == '':
            print(f"Asiento {e+1}: disponible")
        else:
            print(f"Asiento {e+1}: vendido")
    
    for _ in range(cantidad):
        asiento = int(input("Ingres el numero de asiento que dese comprar: ")) - 1
        if asiento < 0 or asiento >= 100:
            print("asiento invalido. intente nuevamente")
            continue
    if asientos[asiento] != '':
        print("asiento no disponible. intente denuevo")
    else:
        tipo_boleto = determinar_tipo_de_boleto(asiento)
        asientos[asiento] = tipo_boleto
        run = input("ingrese su RUN (sin guion ni punto): ")
        asistentes[run] = tipo_boleto
        print("////////////////////////////////////////////")
        print("Operacion realizada bien, :) Boleto comprado")
        print("////////////////////////////////////////////")

def determinar_tipo_de_boleto(asiento):
    if asiento < 20:
        return 'Platinum'
    elif asiento < 50 :
        return 'Gold'
    else:
        return 'Silver'
    
def mostrar_ubicaciones_disponibles():
    print("Estado actual de la venta de entradas: ")
    for e, asiento in enumerate(asientos):
        if asiento == '':
            print(f"asiento {e+1}: disponible")
        else:
            print(f"asiento {e+1}: vendido ({asiento})")

def ver_listado_de_asistentes():
    print("Listado de los asistentes: ")
    for run in sorted(asistentes):
        print(run)

def mostrar_ganacias_totales():
    total = 0
    cantidades = {'Platinum': 0, 'Gold': 0, 'Silver': 0}
    for asiento in asientos:
        if asiento != '':
            cantidades[asiento] += 1
            total += precios[asiento]

    print("tipo entrada / cantidad / total ")
    for tipo, cantidad in cantidades.items():
        total_tipo = precios[tipo * cantidad]
        print(f"{tipo} ${precios[tipo]} / {cantidad} / {total_tipo}")
    print(f"Total / {sum(cantidades.values())} / ${total}")

def principal():
    while True:
        Mostrar_Menu()
        op = input("Seleciones unas de las opciones: ")
#si op(opcion es 1 compra entradas)
        if op == '1':
            compra_de_entradas()
        elif op == '2':
            mostrar_ubicaciones_disponibles()
        elif op == '3':
            ver_listado_de_asistentes()
        elif op == '4':
            mostrar_ganacias_totales()
        elif op == '5':
            print("Ingrese sus datos para inciar salida del sistema.")
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            fecha_actual = datetime.datetime.now().strftime("%d/%m/Y") #fecha de hoy en dia con el import datetime
            print(f"!Un gusto Hasta luego {nombre} {apellido}!!! Salida del sistema: {fecha_actual}")
            break
        else:
            print("!OPCION INVALIDA. INTENTELO NUEVAMENTE!")

principal()


#EthanJoshuaSilvestreBadia 12/07/2023 PGY 1121

