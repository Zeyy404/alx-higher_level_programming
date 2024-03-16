#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host='localhost',
                                 user=sys.argv[1],
                                 password=sys.argv[2],
                                 db=sys.argv[3],
                                 port=3306
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()
