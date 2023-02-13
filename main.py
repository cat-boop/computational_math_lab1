from pathlib import Path
import input_reader
import gauss_solver


def read_data():
    user_choice = int(input("Введите 1 если матрица задается через консоль, либо введите 2 если матрица задается через файл: "))
    while user_choice != 1 and user_choice != 2:
        user_choice = int(input("Введите 1 если матрица задается через консоль, либо введите 2 если матрица задается через файл: "))
    
    if user_choice == 1:
        return input_reader.read_input_data_from_console()

    filename = input("Введите имя файла: ")
    while not Path(filename).is_file():
        filename = input("Файла по такому пути не существует, повторите ввод: ")

    return input_reader.read_input_data_from_file(filename=filename)


if __name__ == "__main__":

    try:
        matrix_size, matrix, accuracy = read_data()

        gauss_solver.solve_matrix_by_gauss_seidel_method(matrix=matrix, matrix_size=matrix_size, accuracy=accuracy)
    except Exception as e:
        print(str(e))
    except KeyboardInterrupt:
        print("Something bad happened...")
