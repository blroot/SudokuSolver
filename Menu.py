from os import system
from Solver import Solver
from FileHandler import FileHandler
from Board import Board
import time
import datetime


class Menu:
    def __init__(self):
        self.menu_options = {
            1: self.solve_from_csv,
            2: self.save_partial,
            3: self.load_partial,
            4: self.test_bench,
            5: exit
        }

    def display_menu(self):
        system('cls')
        print("Bienvenido.... Por favor, seleccione una opción")
        print("1 - Resolver tableros desde archivo CSV")
        print("2 - Guardar ejecución parcial")
        print("3 - Continuar una resolución guardada")
        print("4 - Banco de pruebas")
        print("5 - Salir")

        try:
            option = int(input("Seleccione una opción [1-4]: "))

            option_function = self.menu_options.get(option, None)
            if not option_function:
                print("%s no es una opción válida" % option)
            else:
                option_function()
        except ValueError:
            print("la opción ingresada no corresponde a un número")

    def solve_from_csv(self):
        input_file = str(input("Ingrese la ruta del archivo de entrada: "))
        output_file = str(input("Ingrese la ruta del archivo de salida: "))

        file_handler = FileHandler(input_file, output_file)
        results = {}
        file_handler.read_boards_file_csv()

        try:
            for key in file_handler.boards_dict:
                solver = Solver(file_handler.boards_dict.get(key))
                solver.solve()
                results.setdefault(key, solver.solutions)
        except KeyboardInterrupt:
            dump_name = datetime.datetime.now().strftime("%Y-%b-%d_%H-%M-%S") + ".save"
            self.save_partial(file_handler, dump_name)
            print("Se ha interrumpido la ejecución, dump guardado en %s" % dump_name)
            exit(0)

        file_handler.write_results_to_file(results)
        print("Ha finalizado la resolución! encontrará en %s los resultados" % output_file)

    @staticmethod
    def save_partial(csv_handler, dump_name):
        csv_handler.persist(dump_name)

    def load_partial(self):
        input_file = str(input("Ingrese la ruta del dump de entrada: "))
        output_file = str(input("Ingrese la ruta del archivo de salida: "))

        file_handler = FileHandler(input_file, output_file)
        results = {}
        file_handler.load_boards_file_dump()

        try:
            for key in file_handler.boards_dict:
                solver = Solver(file_handler.boards_dict.get(key))
                solver.solve()
                results.setdefault(key, solver.solutions)
        except KeyboardInterrupt:
            dump_name = datetime.datetime.now().strftime("%Y-%b-%d_%H-%M-%S") + ".save"
            self.save_partial(file_handler, dump_name)
            print("Se ha interrumpido la ejecución, dump guardado en %s" % dump_name)
            exit(0)

        file_handler.write_results_to_file(results)
        print("Ha finalizado la resolución! encontrará en %s los resultados" % output_file)

    def test_bench(self):
        n_list = [9, 16, 25, 36, 49]

        for index, i in enumerate(n_list):
            board = Board([[0 for x in range(i)] for y in range(i)])
            solver = Solver(board, target_solutions=10)
            start = time.time()
            solver.solve()
            end = time.time()
            print("Tablero %sx%s, %s Soluciones" % (i, i, len(solver.solutions)))
            print(solver.solutions)
            print("%s segundos" % str((end-start)/10))


