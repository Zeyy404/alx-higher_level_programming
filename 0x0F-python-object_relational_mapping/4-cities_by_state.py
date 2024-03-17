#!/usr/bin/python3
"""lists all `cities` from the database `hbtn_0e_4_usa`"""
import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(host='localhost',
                                 user=sys.argv[1],
                                 password=sys.argv[2],
                                 db=sys.argv[3],
                                 port=3306)

    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities \
                   INNER JOIN states ON cities.state_id = states.id \
                   ORDER BY cities.id ASC")

    cities = cursor.fetchall()
    for city in cities:
        print(city)

    cursor.close()
    connection.close()
