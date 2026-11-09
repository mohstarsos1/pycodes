def check_is_reversed(s1, s2):
    reversed_s2 = s2[::-1]
    return s1 == reversed_s2


# test
print(check_is_reversed("hel", "leh"))
print(check_is_reversed("heloo", "leh"))
