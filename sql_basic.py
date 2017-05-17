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
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)


def execute_query(sql_query):
    cursor = conn.cursor()
    cursor.execute(sql_query)
    return cursor


def main_menu():
    print('''
    This is the menu.
    1.
    2.
    3.
    4.
    5.
    6.
    7.
    Gimme an input:''')
    answer = input('> ')
    while answer != '8':
        answer = input('> ')
        if answer == '1':
            cursor = execute_query("""
                                   SELECT first_name,last_name
                                   FROM mentors;
                                   """)
            rows = cursor.fetchall()
            print(tabulate(rows, headers=[desc[0] for desc in cursor.description]))
            print('\n')

        elif answer == '2':
            cursor = execute_query("""
                                   SELECT nick_name
                                   FROM mentors
                                   WHERE city='Miskolc';
                                   """)
            rows = cursor.fetchall()
            print(tabulate(rows, headers=[desc[0] for desc in cursor.description]))
            print('\n')

        elif answer == '3':
            cursor = execute_query("""
                                   SELECT CONCAT(first_name, ' ', last_name), phone_number
                                   FROM applicants
                                   AS full_name
                                   WHERE first_name='Carol';
                                   """)
            rows = cursor.fetchall()
            print(tabulate(rows, headers=['full_name', 'phone_number']))
            print('\n')

        elif answer == '4':
            cursor = execute_query("""
                                   SELECT CONCAT(first_name, ' ', last_name), phone_number
                                   FROM applicants
                                   AS full_name
                                   WHERE email
                                   LIKE '%@adipiscingenimmi.edu';
                                   """)
            rows = cursor.fetchall()
            print(tabulate(rows, headers=['full_name', 'phone_number']))
            print('\n')

        elif answer == '5':
            cursor = execute_query("""
                                   INSERT INTO applicants (first_name, last_name, phone_number, 
                                   email, application_code)
                                   VALUES ('Markus', 'Schaffarzyk', '003620/725-2666',
                                   'djnovus@groovecoverage.com', 54823);
                                   """)
            cursor = execute_query("""
                                   SELECT *
                                   FROM applicants
                                   WHERE application_code='54823';""")
            rows = cursor.fetchall()
            print(tabulate(rows, headers=[desc[0] for desc in cursor.description]))
            print('\n')

        elif answer == '6':
            cursor = execute_query("""
                                   UPDATE applicants
                                   SET phone_number='003670/223-7459'
                                   WHERE first_name='Jemima' AND last_name='Foreman';
                                   """)
            cursor = execute_query("""
                                   SELECT *
                                   FROM applicants
                                   WHERE first_name='Jemima' AND last_name='Foreman';""")
            rows = cursor.fetchall()
            print(tabulate(rows, headers=[desc[0] for desc in cursor.description]))
            print('\n')
        elif answer == '7':
            cursor = execute_query("""DELETE FROM applicants WHERE email LIKE '%mauriseu.net';""")
            cursor = execute_query("""
                                   SELECT *
                                   FROM applicants;""")
            rows = cursor.fetchall()
            print(tabulate(rows, headers=[desc[0] for desc in cursor.description]))
            print('\n')
main_menu()