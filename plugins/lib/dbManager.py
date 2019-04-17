import pyodbc


class DBManager(object):
    __db_connector = None
    driver = ""
    server = ""
    database = ""
    user = ""
    password = ""

    @classmethod
    def connect_to_db(cls, driver, server, database, user, password):
        cls.driver = driver
        cls.server = server
        cls.database = database
        cls.user = user
        cls.password = password

        cls.get_connection()

    @classmethod
    def get_connection(cls, new=False):
        """Creates return new Singleton database connection.
        If new=True, it will create new db connection (e.g. in case of timeout)"""
        if new or not cls.__db_connector:
            cls.__db_connector = DBManager().create_connection()
        return cls.__db_connector

    @classmethod
    def execute_query(cls, query):
        """execute query on singleton db connection"""
        print("Executing query:" + query)
        res = ""

        cursor = cls.get_cursor()

        try:
            cursor.execute(query)
        except pyodbc.ProgrammingError as e:
            print("Could not execute the query:" + str(e))

        try:
            res = cursor.fetchall()
        except pyodbc.ProgrammingError:
            print("No return value from db")

        cursor.commit()
        cursor.close()
        return res

    @classmethod
    def get_cursor(cls):
        """Used for querying DB"""
        connection = cls.get_connection()
        try:
            cursor = connection.cursor()
        except pyodbc.ProgrammingError:
            connection = cls.get_connection(new=True)  # Create new connection
            cursor = connection.cursor()
        return cursor

    @classmethod
    def build_table(cls, table_name, *args):
        """
        This method creates table called <table_name>
        It contains variables *args
        Example use:
        build_table("Employee", "ID int", "Name varchar(255)")
        """
        query="CREATE TABLE {} (".format(table_name)
        for i, arg in enumerate(args):
            if len(args) != i+1:
                query += arg + ", "
            else:
                query += arg + ");"
        cls.execute_query(query)

    @classmethod
    def display_table(cls, table_name):
        query = "select * from {}".format(table_name)
        rows = cls.execute_query(query)
        print("Table: " + table_name)
        for row in rows:
            print(row)

    # creates new connection
    @classmethod
    def create_connection(cls):
        return pyodbc.connect("DRIVER={}".format(cls.driver) + \
                              "SERVER={}".format(cls.server) + \
                              "DATABASE={}".format(cls.database) + \
                              "UID={}".format(cls.user) + \
                              "PWD={}".format(cls.password))
