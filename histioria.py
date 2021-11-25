def cuento1 ():
    hisotria1 = "Habia una vez un chile que queira ______ pero no podia porque el era _____ pero su mama le decia que el siempre seria _____"
    print(hisotria1)
    palabra1: str = input("escribe la pirimer palabra: ")
    palabra2: str = input("escribe la segunda palabra: ")
    palabra3: str = input("escribe la tercer palabra: ")
    print("Tu historia es:")
    print("habia una vez un chile que queria " + palabra1 + " pero no podia porque el era " + palabra2 + " pero su mama le decia que el simepre seria " + palabra3)

def cuento2 ():
    historia2 = "En un pueblo lejano llamado _____ existia un hombre llamado _____ que secuestraba personas para quemarlas y comerselas con ______ pero ntp solo lo hace si conoces su nombre"
    print(historia2)
    palabra1: str = input("escribe la primer palabra: ")
    palabra2: str = input("escribe la segunda palabra: ")
    palabra3: str = input("escribe la tercer palabra: ")
    print("tu historia es: ")
    print("En un pueblo lejano llamado " + palabra1 + " existia un hombre llamado " + palabra2 + " que secuestraba personas para quemarlas y comerselas con " + palabra3 + " pero ntp solo lo hace si conoces su nombre" )


def run():
    try:

        menu = """
        Bienvenido a historias locas , selecciona una opcion escribiendo 1 o 2: 
        1.- Historia chistosa.
        2 - Historia de miedo.
        """
        opcion = int(input(menu))
        if opcion == 1:
            cuento1()
        elif opcion == 2:
            cuento2 ()
        else:
            print("eres subnormal? debes elegir una opcion correcta")
    except ValueError:
        print("Solo puedes escribir numeros")

    



if __name__== "__main__":
    run()