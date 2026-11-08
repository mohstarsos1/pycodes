def sum_of_even_items(list):
    sum = 0
    for item in list:
        if item % 2 == 0:
            sum += item
    return sum


# test
print(sum_of_even_items([1, 2, 5, 6, 3, 8, 9]))
