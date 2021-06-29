import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "ems.db"

    sql_create_position_table = """CREATE TABLE position(positionId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,positionName VARCHAR NOT NULL,startingRate numeric NOT NULL,active BOOLEAN,createdAt DATE,updatedAt DATE)"""

    sql_create_employees_table = """CREATE TABLE employees(employeeId integer PRIMARY KEY AUTOINCREMENT NOT NULL,socialsecuritynumber INTEGER NOT NULL,firstName VARCHAR NOT NULL,middleInitial VARCHAR,lastName VARCHAR NOT NULL,addressLine1 VARCHAR NOT NULL,addressLine2 VARCHAR NOT NULL,mobilePhone VARCHAR NOT NULL,alternatePhone VARCHAR NOT NULL,maritialStatus VARCHAR NOT NULL,gender VARCHAR NOT NULL,hiredDate DATE NOT NULL,resignationDate DATE NOT NULL,terminationReason VARCHAR,currentRate numeric ,positionId integer,active boolean,createdAt DATE,updatedAt DATE,FOREIGN KEY (positionId) REFERENCES position (positionId))"""
    
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_position_table)

        # create tasks table
        create_table(conn, sql_create_employees_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()