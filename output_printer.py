import math

def print_matrix(matrix: list[list[float]]) -> None:
    for matrix_row in matrix:
        for row_value in matrix_row:
            print(row_value, end = " ")
        print()

def print_iteration_values_accuracy(current_iteration: int, values: list[float], accuracy: float = float('nan')) -> None:
    print("{:-3d} | ".format(current_iteration), end="")
    for value in values:
        print("{:7.4f} | ".format(value), end="")
    
    if math.isnan(accuracy):
        print("    -")
    else:
        print("{:7.4f}".format(accuracy))
