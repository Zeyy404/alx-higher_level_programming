#!/usr/bin/python3
"""takes in an argument and displays all values in the `states`
    table of `hbtn_0e_0_usa` where name matches the argument.
   safe from MySQL injections!"""
import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(host='localhost',
                                 user=sys.argv[1],
                                 password=sys.argv[2],
                                 db=sys.argv[3],
                                 port=3306)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY id ASC", {'name': sys.argv[4]})

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    connection.close()
