def pow_list(l):
    powered_list = []
    for item in l:
        powered_list.append(item**2)
    return powered_list


# test
print(pow_list([1, 2, 3, 4, 5]))
