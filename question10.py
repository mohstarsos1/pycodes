def repeat_count_chars_in_string(s):
    dict = {}
    for char in s:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    return dict


# test
print(repeat_count_chars_in_string("hello"))
