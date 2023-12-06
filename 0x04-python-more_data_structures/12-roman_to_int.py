#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    list_keys = [rom_num[x] for x in roman_string]
    integer = 0
    if roman_string:
        for y in range(len(list_keys)):
            integer += list_keys[y]
            if list_keys[y] > list_keys[y - 1] and y != 0:
                integer -= list_keys[y - 1] * 2
        return integer
    if not isinstance(roman_string, str):
        return 0
    if not roman_string:
        return 0
