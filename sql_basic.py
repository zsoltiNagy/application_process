import psycopg2
from tabulate import tabulate  # https://pypi.python.org/pypi/tabulate

try:
    # setup connection string
    connect_str = "dbname='szabadon' user='szabadon' host='localhost' password='pringles'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)


def execute_sql_statement(sql_statement):
    cursor = conn.cursor()
    cursor.execute(sql_statement)
    return cursor


def main_menu():
    print('''
    Dear HR, this is the menu.
    1. Returns the two name columns of the mentors table.
    2. Returns the nick_name-s of all mentors working at Miskolc.
    3. Returns Carols full name and telephone number.
    4. Returns full name and telephone number of the gril who went to Adipiscingenimmi University.
    5. Inserts a new row for Markus Schaffarzyk into the applicants table.
    6. Updates Jemima Foremans telephone number.
    7. Deletes everybody from the applicants table with 'mauriseu.net' domain name in their email address.
    8. Deletes row from applicants with application_number 54823.
    0. Quits the program.
    Choose a number from the above list:''')
    answer = 666
    while answer != '0':
        answer = input('> ')
        if answer == '1':
            cursor = execute_sql_statement("""
                                   SELECT first_name,last_name
                                   FROM mentors;
                                   """)
            rows = cursor.fetchall()
            print(tabulate(rows, headers=[desc[0] for desc in cursor.description]))
            print('\n')

        elif answer == '2':
            cursor = execute_sql_statement("""
                                   SELECT nick_name
                                   FROM mentors
                                   WHERE city='Miskolc';
                                   """)
            rows = cursor.fetchall()
            print(tabulate(rows, headers=[desc[0] for desc in cursor.description]))
            print('\n')

        elif answer == '3':
            cursor = execute_sql_statement("""
                                   SELECT CONCAT(first_name, ' ', last_name), phone_number
                                   FROM applicants
                                   AS full_name
                                   WHERE first_name='Carol';
                                   """)
            rows = cursor.fetchall()
            print(tabulate(rows, headers=['full_name', 'phone_number']))
            print('\n')

        elif answer == '4':
            cursor = execute_sql_statement("""
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
            cursor = execute_sql_statement("""
                                   INSERT INTO applicants (first_name, last_name, phone_number, 
                                   email, application_code)
                                   VALUES ('Markus', 'Schaffarzyk', '003620/725-2666',
                                   'djnovus@groovecoverage.com', 54823);
                                   """)
            cursor = execute_sql_statement("""
                                   SELECT *
                                   FROM applicants
                                   WHERE application_code='54823';""")
            rows = cursor.fetchall()
            print(tabulate(rows, headers=[desc[0] for desc in cursor.description]))
            print('\n')

        elif answer == '6':
            cursor = execute_sql_statement("""
                                   UPDATE applicants
                                   SET phone_number='003670/223-7459'
                                   WHERE first_name='Jemima' AND last_name='Foreman';
                                   """)
            cursor = execute_sql_statement("""
                                   SELECT *
                                   FROM applicants
                                   WHERE first_name='Jemima' AND last_name='Foreman';""")
            rows = cursor.fetchall()
            print(tabulate(rows, headers=[desc[0] for desc in cursor.description]))
            print('\n')
        elif answer == '7':
            cursor = execute_sql_statement("""DELETE FROM applicants WHERE email LIKE '%mauriseu.net';""")
            cursor = execute_sql_statement("""
                                   SELECT *
                                   FROM applicants;""")
            rows = cursor.fetchall()
            print(tabulate(rows, headers=[desc[0] for desc in cursor.description]))
            print('\n')
        elif answer == '8':
            cursor = execute_sql_statement("""DELETE FROM applicants WHERE application_code='54823';""")
            cursor = execute_sql_statement("""
                                   SELECT *
                                   FROM applicants;""")
            rows = cursor.fetchall()
            print(tabulate(rows, headers=[desc[0] for desc in cursor.description]))
            print('\n')
main_menu()