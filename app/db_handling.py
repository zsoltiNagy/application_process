import psycopg2
# from tabulate import tabulate  source: https://pypi.python.org/pypi/tabulate probably won't need it, kepping it though


def execute_sql_statement(sql_statement, values=tuple()):
    # setup connection string, not the most secure way
    connect_str = "dbname=szabadon user=szabadon host=localhost password=pringles"
    # we create this variable by assigning a None value to it,
    # so when an Exception is catched, the function will not try to close a non-existing variable
    conn = None
    try:
        # use our connection values assigned to the connection string to establish a connection
        # Hey dawg, I heard you like connection, so I put your connection values into your connection string to
        # use them to establish a connection
        conn = psycopg2.connect(connect_str)
    except Exception as e:  # TODO don't use this, remember: "raise PythonicError("Errors should never go silently.")
        print(e)
    else:
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(sql_statement, values)
        if sql_statement[:6].lower() == 'select':
            rows = list(cursor.fetchall())
            return rows
    finally:
        if conn:
            # conn.commit() leaving it here for future testing to see how it works
            conn.close()


# keeping it so if I need it I can reuse it easily
'''
def print_db_table(rows):
    print(tabulate(rows, headers=[desc[0] for desc in cursor.description]))
    print('\n')
'''
