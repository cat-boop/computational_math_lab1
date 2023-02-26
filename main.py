from pathlib import Path
import input_reader
import gauss_solver


def read_data():
    try:
        user_choice = int(input("Введите 1 если матрица задается через консоль, либо введите 2 если матрица задается через файл, либо 3 если матрица задается случайным образом: "))
        while user_choice not in [1, 2, 3]:
            user_choice = int(input("Введите 1 если матрица задается через консоль, либо введите 2 если матрица задается через файл, либо 3 если матрица задается случайным образом: "))
    except ValueError:
        raise ValueError("Введенная строка не является числом")

    if user_choice == 1:
        return input_reader.read_input_data_from_console()

    if user_choice == 2:
        filename = input("Введите имя файла: ")
        while not Path(filename).is_file():
            filename = input("Файла по такому пути не существует, повторите ввод: ")

        return input_reader.read_input_data_from_file(filename=filename)
    
    return input_reader.generate_matrix()


if __name__ == "__main__":
    try:
        matrix_size, matrix, accuracy = read_data()

        print("Введенная матрица: ")
        for matrix_row in matrix:
            print(*matrix_row)

        gauss_solver.solve_matrix_by_gauss_seidel_method(matrix=matrix, matrix_size=matrix_size, accuracy=accuracy)
    except Exception as e:
        print(str(e))
        print("Программа завершена")
    except KeyboardInterrupt:
        print("\nПрограмма завершена из-за неправильного ввода")
