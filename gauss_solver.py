import output_printer

def is_matrix_diagonalized(matrix: list[list[float]], matrix_size: int) -> bool:
    number_of_correct_rows = 0
    strict_conidition_for_one_of_rows_is_done = False
    for i, matrix_row in enumerate(matrix):
        row_sum = 0
        for j, matrix_value in enumerate(matrix_row[:-1]):
            if i != j:
                row_sum += abs(matrix_value)
        if abs(matrix_row[i]) >= row_sum:
            number_of_correct_rows += 1
        if abs(matrix_row[i]) > row_sum:
            strict_conidition_for_one_of_rows_is_done = True
    return number_of_correct_rows == matrix_size and strict_conidition_for_one_of_rows_is_done


def diagonalize_matrix(matrix: list[list[float]], matrix_size: int) -> None:
    if is_matrix_diagonalized(matrix=matrix, matrix_size=matrix_size):
        return
    
    possible_row_locations = [[] for _ in range(matrix_size)]
    for i, matrix_row in enumerate(matrix):
        row_sum = sum([abs(value) for value in matrix_row[:-1]])

        for j, row_value in enumerate(matrix_row[:-1]):
            if abs(row_value) > row_sum - abs(row_value):
                possible_row_locations[j].append(i)

    # print(possible_row_locations)

    new_matrix = [[] for _ in range(matrix_size)]
    if try_to_place_rows(possible_row_locations, 0, matrix, new_matrix):
        matrix[::] = new_matrix[::]


def try_to_place_rows(possible_row_locations: list[list[int]], current_index: int, old_matrix: list[list[float]], new_matrix: list[list[float]]) -> bool:
    if current_index == len(possible_row_locations):
        return True

    for possible_row_location in possible_row_locations[current_index]:
        if len(new_matrix[current_index]) == 0:
            new_matrix[current_index] = old_matrix[possible_row_location]
            
            if try_to_place_rows(possible_row_locations, current_index + 1, old_matrix, new_matrix):
                return True
    return False


def solve_matrix_by_gauss_seidel_method(matrix: list[list[float]], matrix_size: int, accuracy: float) -> list[float]:
    diagonalize_matrix(matrix=matrix, matrix_size=matrix_size)
    
    if is_matrix_diagonalized(matrix=matrix, matrix_size=matrix_size):
        print("Условие преобладания диагональных элементов достигнуто: ")
        output_printer.print_matrix(matrix)
    else:
        print("Условие преобладания диагональных элементов не достигнуто")

    max_iterations = 100
    current_iteration = 0

    c = []
    d = []

    for i, matrix_row in enumerate(matrix):
        next_c_vector = []
        for j, row_value in enumerate(matrix_row[:-1]):
            if i == j:
                next_c_vector.append(0)
            else:
                if matrix_row[i] == 0:
                    raise ValueError("Значения на диагонали матрицы не могут быть равны 0")
                next_c_vector.append(-1 * row_value / matrix_row[i])
        c.append(next_c_vector)
        d.append(matrix_row[-1] / matrix_row[i])

    print("Вектор неизвестных:")
    print(c)
    print(d)

    x_k = [value for value in d]

    # output_printer.print_iteration_values_accuracy(current_iteration=current_iteration, values=x_k)

    accuracy_vector = []
    max_accuracy = 100
    while max_accuracy > accuracy and current_iteration < max_iterations:
        current_iteration += 1
        next_x_k = []
        for i in range(matrix_size):
            next_x_k_value = d[i]
            for j in range(i):
                next_x_k_value += c[i][j] * next_x_k[j]
            for j in range(i, matrix_size):
                next_x_k_value += c[i][j] * x_k[j]
            next_x_k.append(next_x_k_value)
    
        accuracy_vector = [abs(next_x_k[i] - x_k[i]) for i in range(matrix_size)]
        max_accuracy = round(max(accuracy_vector), 5)
        x_k = [round(value, 5) for value in next_x_k]

        # output_printer.print_iteration_values_accuracy(current_iteration=current_iteration, values=x_k, accuracy=max_accuracy)
    
    print("Ответ найден за {} итераций: ".format(current_iteration))
    print(x_k)
    print("Вектор погрешностей:")
    print(accuracy_vector)

    