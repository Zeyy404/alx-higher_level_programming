#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    r_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    if roman_string:
        for i in range(len(roman_string)):
            c_v = r_num[roman_string[i]]
            n_v = r_num[roman_string[i + 1]] if i + 1 < len(roman_string) else 0

            if c_v < n_v:
                integer -= c_v
            else:
                integer += c_v

        return integer
    else:
        return 0
