from CsvLoader import CsvLoader
from exceptions import InvalidRowLength, NotAnInteger, NotAValidInteger
from Solver import Solver


if __name__=="__main__":
    loader = CsvLoader()
    try:
        results = {}
        loader.read_boards_file()
        for key in loader.boards_dict:
            solver = Solver(loader.boards_dict.get(key))
            solver.solve()
            results.setdefault(key, solver._solutions)
        print(results)

    except InvalidRowLength as e:
        print("La fila %s no tiene la dimensión correcta" % e.row_number)
    except NotAnInteger:
        print("Se ha ingresado un caracter no entero")
    except NotAValidInteger:
        print("Solo se aceptan números enteros del 0 al 9")
    finally:
        print("El programa ha finalizado")
