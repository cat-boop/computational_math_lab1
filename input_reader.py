import random

def generate_matrix() -> tuple[int, list[list[float]]]:
    print("Введите размерность матрицы: ", end="")
    matrix_size = read_matrix_size_from(input)

    matrix = []
    for i in range(matrix_size):
        matrix_row = []
        for _ in range(matrix_size - 1):
            matrix_row.append(round(random.uniform(-100, 100), 4))
        
        row_sum = sum([abs(row_value) for row_value in matrix_row])
        matrix_row.append(round(random.uniform(row_sum, row_sum * 2), 4))
        matrix_row[i], matrix_row[-1] = matrix_row[-1], matrix_row[i]

        matrix_row.append(round(random.uniform(-100, 100), 4))

        matrix.append(matrix_row)
    
    print("Введите желаемую точность: ", end="")
    accuracy = read_accuracy_from(input)

    return matrix_size, matrix, accuracy


def read_input_data_from_console() -> tuple[int, list[list[float]]]:
    print("Введите размерность матрицы: ", end="")
    matrix_size = read_matrix_size_from(input)

    print("Введите матрицу:")
    matrix = read_matrix_from(input, matrix_size)

    print("Введите желаемую точность: ", end="")
    accuracy = read_accuracy_from(input)

    return matrix_size, matrix, accuracy


def read_input_data_from_file(filename: str) -> tuple[int, list[list[float]]]:
    file = open(filename, "r", encoding="UTF-8")

    matrix_size = read_matrix_size_from(file.readline)
    matrix = read_matrix_from(file.readline, matrix_size)
    accuracy = read_accuracy_from(file.readline)

    return matrix_size, matrix, accuracy


def read_accuracy_from(input_stream) -> float:
    try:
        accuracy = float(input_stream())
        if accuracy <= 0:
            raise ArithmeticError("Точность должна быть положительным числом большим 0")
        return accuracy
    except ValueError:
        raise ValueError("Введенная строка не является числом с плавающей точкой")


def read_matrix_size_from(input_stream) -> int:
    try:
        matrix_size = int(input_stream())
        if matrix_size <= 0 or matrix_size > 20:
            raise ArithmeticError("Порядок матрицы должен быть положительным числом не большим 20")
        return matrix_size
    except ValueError:
        raise ValueError("Введенная строка не является целым числом")

def read_matrix_from(input_stream, matrix_size) -> list[list[float]]:
    matrix = []

    for _ in range(matrix_size):
        try :
            row = list(map(float, input_stream().strip().split()))
            if len(row) != matrix_size + 1:
                raise ArithmeticError("Количество элементов в строке матрицы должно быть равным {}".format(matrix_size + 1))
            matrix.append(row)
        except ValueError:
            raise ValueError("Введенная строка не является числом с плавающей точкой")
            
    return matrix