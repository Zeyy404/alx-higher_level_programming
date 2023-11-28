#!/usr/bin/python3
for i in range(26):
    print("{}".format(chr(ord('z' if i % 2 == 0 else 'Z') - i)), end="")
