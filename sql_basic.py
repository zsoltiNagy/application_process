import psycopg2


def make_first_steps():
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


def get_querry():
    '''
    A function to automatize the process of get querys from the table.
    It should be a class?
    '''
    pass

make_first_steps()
get_querry()