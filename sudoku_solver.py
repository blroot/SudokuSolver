from CsvHandler import CsvHandler
from exceptions import InvalidRowLength, NotAnInteger, NotAValidInteger
from Solver import Solver


if __name__=="__main__":
    csv_handler = CsvHandler("tableros.csv", "resultados.csv")
    try:
        results = {}
        csv_handler.read_boards_file()
        for key in csv_handler.boards_dict:
            solver = Solver(csv_handler.boards_dict.get(key))
            solver.solve()
            results.setdefault(key, solver._solutions)

        csv_handler.write_results_to_file(results)

    except InvalidRowLength as e:
        print("La fila %s no tiene la dimensión correcta" % e.row_number)
    except NotAnInteger:
        print("Se ha ingresado un caracter no entero")
    except NotAValidInteger:
        print("Solo se aceptan números enteros del 0 al 9")
    finally:
        print("El programa ha finalizado")
