import psycopg2
from tabulate import tabulate  # https://pypi.python.org/pypi/tabulate

try:
    # setup connection string
    connect_str = "dbname='szabadon' user='szabadon' host='localhost' password='pringles'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)


def execute_querry(sql_query, headers):
    '''
    A function to automatize the process of get querys from the table.
    It should be a class?
    '''
    # I could write a regex or something similar for this headers stuff
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    print(tabulate(rows, headers=headers))

execute_querry("""SELECT first_name, last_name FROM mentors;""", ['first_name', 'last_name'])