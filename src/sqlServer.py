import pyodbc
from yamlRead import yamlReader

yr = yamlReader("config/server.yaml")
userData = yr.data
SERVER = userData['SERVER']
DATABASE = userData['DATABASE']
USERNAME = userData['USERNAME']
PASSWORD = userData['PASSWORD']

# create an object to handle pyodbc
class SQLConnector():
    _connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
    _connection = None
    _cursor = None
    schema_name = ""
    columns = {}

    def __init__(self):
        self.connect()

    def connect(self):
        self._connection = pyodbc.connect(self._connectionString)
        self._cursor = self._connection.cursor()

    # Close the connection when finished
    def close(self) -> None:
        self._connection.close()
        self._connetion = None
        self._cursor = None


    def clearData(self):
        self.columns = []
        self.schema_name = ""

    def _submitquery(self, connection_string:str=None):
        # Submit a passed sql query and return the result
        if connection_string == None: raise Exception("missing argument 'connection_string` submit sql query")
        self._cursor.execute(connection_string)
        res = self._cursor.fetchall()
        # return object
        return res

    # This will fill the self.columns dictionary
    # Returns a list of the headers
    def fetchSchema(self, schema_name:str) -> list:
        if self.schema_name=="": self.schema_name = schema_name
        else: raise Exception("clear data before fetching new")

        # Extract the id of the desired schema
        headerid = self._submitquery(f"select id from excelschemas s where s.schemaname = '{schema_name}'")[0][0]
        # the headers will be Keys and the datatypes will be values
        headers = self._submitquery(f"select column_name from excelschemas_datatypes d where d.excelschema_id = {headerid}")
        headers = [h[0] for h in headers]

        # Loop through the datatypes adding each with its corresponding key to self.columns
        for header in headers:
            datatype = self._submitquery(f"select datatype_regex from excelschemas_datatypes d where d.column_name = '{header}'")[0][0]
            self.columns[header] = datatype
        return headers

    # Returns a list the same as that returned in fetchSchema, however this can be run twice
    def get_headers(self) -> list:
        # Return the headers (keys) of the self.columns dict
        lst = []
        for key in self.columns.keys():
            lst.append(key)
        return lst


if __name__ == "__main__":
    test = SQLConnector()
    test.fetchSchema("userdb")
    test.close()