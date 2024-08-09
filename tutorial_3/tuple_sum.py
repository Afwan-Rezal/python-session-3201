tup = (1, 2, 3, 4, 5, 6, 7)


def sum_of_tuples(tuple):
    sum = 0
    max_limit = int(len(tuple))
    for i in range(max_limit):
        sum = int(tuple[i] + sum)
    return sum

print(sum_of_tuples(tup))