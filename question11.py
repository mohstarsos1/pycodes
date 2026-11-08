def avg_of_list(l):
    sum = 0
    for item in l:
        sum += item
    return sum / len(l)


# test
print(avg_of_list([1, 2, 3, 4, 5, 6]))
