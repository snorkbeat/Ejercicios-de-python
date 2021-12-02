from datetime import datetime
import pytz


def año_bis():
    año = int(input("Ingresa el año que quieres saber: "))
    if año % 100 != 0 and año % 400 != 0:
        print(" El año es bisiesto estoy mamadisimo htpm")
        print(" Aqui acaba el programa")
    else:
        print(" NO es un año bisiesto")
        print(" Aqui acaba el programa")

def lis_año():
    año1 = int(input(" escribe el primer año"))
    año2 = int(input(" escribe el segundo año"))
    bisi = [i for i in range (año1, año2) if i % 100 !=0 and i % 400 !=0]
    print(bisi)



def run():
    try:

        menu = """
         xxxx - x    x -  xxx  - xxxx  - x   x  -
        x     - xx   x - x   x - x   x - x  x   -
         xxx  - x x  x - x   x - xxxx  - xxx    -
            x - x  x x - x   x - x  x  - x  x   -
        xxxx  - x   xx -  xxx  - x   x - x    x -

        Bienvenido al calculador de años bisisestos escribe el numero de la opcion que deseas: 
        1.- Saber si un año en especifico es bisiesto.
        2 - Saber los años bisiestos en un rango de x años a x años escribiendo primero el menor y despues el mayor.
        
        : """
        mexico_timmezone = pytz.timezone("America/Mexico_City")
        mexico_date = datetime.now(mexico_timmezone)
        print("Ciudad de Mexico:", mexico_date.strftime("%d/%m/%y, %H:%M:%S" ))

        opcion = int(input(menu))
        if opcion == 1:
            año_bis()
        elif opcion == 2:
            lis_año()
        else:
            print("no sabes leer ? elige una opcion correcta")
    except ValueError:
        print("Solo puedes escribir numeros")


if __name__ == "__main__":
    run()
