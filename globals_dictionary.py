
def sum_of_two_numbers(num_1, num_2):
    return num_1 + num_2


def mult_of_two_numbers(num_1, num_2):
    return num_1 * num_2


all_math_operations = [globals()[name] for name in globals()
                       if name.endswith('numbers')]


def math_operations(val_1, val_2):
    return list(operation(val_1, val_2) for operation in all_math_operations)


print(math_operations(2, 3))

