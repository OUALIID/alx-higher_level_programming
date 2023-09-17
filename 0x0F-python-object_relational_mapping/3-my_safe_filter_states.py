#!/usr/bin/python3
"""
Same code as previous. But this time, safe from MySQL injections!
"""
import MySQLdb
import sys


def main():
    args = sys.argv[1:]
    username = args[0]
    password = args[1]
    database = args[2]
    state_name = args[3]
    connection = MySQLdb.connect(
        user=username,
        password=password,
        db=database,
        host="localhost",
        port=3306,

    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s "
                   "ORDER BY id ASC;", (state_name + "%",))
    for i in cursor.fetchall():
        print(i)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
