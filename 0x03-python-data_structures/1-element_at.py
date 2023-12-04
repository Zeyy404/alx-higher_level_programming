#!/usr/bin/python3
def element_at(my_list, idx):
    len_list = len(my_list) - 1
    if idx < 0:
        return None
    if idx > len_list:
        return None
    return (my_list[idx])
