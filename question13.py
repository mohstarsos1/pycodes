def delete_repeat_num_from_list(l):
    new_list = []
    for item in l:
        if item not in new_list:
            new_list.append(item)
    return new_list


# test
print(delete_repeat_num_from_list([1, 1, 2, 3, 3, 5, 1, 3, 9, 8]))
