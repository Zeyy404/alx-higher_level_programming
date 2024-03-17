#!/usr/bin/python3
"""takes in the name of a state as an argument and
   lists all cities of that state, using the database hbtn_0e_4_usa"""
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
                   JOIN states ON cities.state_id = states.id \
                   WHERE states.name LIKE BINARY %s \
                   ORDER BY cities.id ASC", (sys.argv[4],))

    cities = cursor.fetchall()
    if cities:
        print(", ".join(city[1] for city in cities))

    cursor.close()
    connection.close()
