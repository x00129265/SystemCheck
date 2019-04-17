import pyodbc

class DBConnector(object):

    def __init__(self, driver, server, database, user, password):

        self.driver = driver
        self.server = server
        self.database = database
        self.user = user
        self.password = password
        self.dbconn = None

    # creats new connection
    def create_connection(self):
        return pyodbc.connect("DRIVER={};".format(self.driver) + \
                              "SERVER={};".format(self.server) + \
                              "DATABASE={};".format(self.database) + \
                              "UID={};".format(self.user) + \
                              "PWD={};".format(self.password) + \
                              "CHARSET=UTF8",
                              ansi=True)

    # For explicitly opening database connection
    def __enter__(self):
        self.dbconn = self.create_connection()
        return self.dbconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbconn.close()