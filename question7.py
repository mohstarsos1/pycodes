def find_max_length_in_list(l):
    max_length = l[0]
    for item in l:
        if len(item) > len(max_length):
            max_length = item
    return max_length


# test
print(find_max_length_in_list(["a", "aabb", "aaabbb", "bb"]))
