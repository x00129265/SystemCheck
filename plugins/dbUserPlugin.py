from plugins.pluggable import Pluggable
from plugins.lib.dbManager import DBManager


class Plugin(Pluggable):
    def __init__(self):
        self.db = DBManager()
        self.db.connect_to_db(driver='SQL Server;',
                              database='HuaweiInterview;',
                              server='tcp:x00129265.database.windows.net,1433;',
                              user='janistihonovs;',
                              password='myInterview123;')

    def _execute(self):
        # Display data
        rows = DBManager().execute_query("SELECT name FROM sys.database_principals")
        for row in rows:
            print(row)
