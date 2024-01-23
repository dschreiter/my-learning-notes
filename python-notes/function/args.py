def sum_of(*args):
    sum = 0
    for curr_val in args:
        sum += curr_val
    return sum


print(sum_of(5, 5, 5, 4))  # can pass any number of args, very cool
