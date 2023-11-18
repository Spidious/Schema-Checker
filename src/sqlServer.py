import pyodbc

'''
SERVER = '<server-address>'
DATABASE = '<database-name>'
USERNAME = '<username>'
PASSWORD = '<password>'
'''

# Connection attributes
SERVER = 'LUKES-DESKTOP'
DATABASE = 'schemas'
# USERNAME = '<username>'
# PASSWORD = '<password>'
    

# create an object to handle pyodbc
class SQLConnector():
    _connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
    _connection = None
    _cursor = None
    _schema: str = None
    tables: object = []

    def __init__(self, schemaName: str = None):
        # Raise specific exception if schema is not defined
        if schemaName == None: raise Exception("No schema name was provided")
        
        #Define the cursor and connection
        self._schema = schemaName
        self._connection = pyodbc.connect(self._connectionString)
        self._cursor = self._connection.cursor()

    # Close the connection when finished
    def close(self) -> None:
        self._connection.close()

    # fill self.tables with Table objects (only the names)
    def fetchTables(self):        
        # Query to retrieve tables
        squery = f"select TABLE_NAME from {self._schema}.TABLES"
        self._cursor.execute(squery)
        res = self._cursor.fetchall()
        res = [i[0] for i in res]

        # Create tables with empty schema
        self.tables = [Table(name) for name in res]
        
        

class Table(object):
    tableName = None
    schema = {}

    def __init__(self, name: str, schemas: list = [], types: list = []):
        # Assert that the schemas should be the same lenght as types
        if len(schemas)!=len(types): raise Exception("ERROR: list `schemas` length does not match `types` length. Potential loss of data.")

        self.tableName = name

        # For every element in schemas
        for i in range(0, len(schemas)):
            self.schema[schemas[i]] = types[i]
    