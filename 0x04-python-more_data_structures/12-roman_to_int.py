#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    if roman_string:
        integer = rom_num[roman_string[0]]
        for char in roman_string[1:]:
            if rom_num[char] > integer:
                integer = rom_num[char] - integer
            else:
                integer += rom_num[char]
        return integer
    else:
        return 0
