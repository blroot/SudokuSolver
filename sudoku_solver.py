from exceptions import InvalidRowLength, NotAnInteger, NotAValidInteger
from Menu import Menu


if __name__ == "__main__":
    try:
        menu = Menu()
        while True:
            menu.display_menu()

    except InvalidRowLength as e:
        print("La fila %s no tiene la dimensión correcta" % e.row_number)
    except NotAnInteger:
        print("Se ha ingresado un caracter no entero")
    except NotAValidInteger:
        print("Solo se aceptan números enteros del 0 al 9")
    finally:
        print("El programa ha finalizado")
