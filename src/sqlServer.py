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
    _schema: str
    tables = []

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

    # overwrite self.tables with Table objects (only the names)
    def fetchTables(self):        
        # Query to retrieve tables
        squery = f"select TABLE_NAME from {self._schema}.TABLES"
        self._cursor.execute(squery)
        res = self._cursor.fetchall()
        res = [i[0] for i in res]

        # Create tables with empty schema
        self.tables=[Table(name) for name in res]


    # fill the schemas of the Tables in self.table
    def fetchSchema(self):
        # for each table in self.tables
        for table in self.tables:
            # Query the database for the Column_Name and Data_Type
            squery = f"select COLUMN_NAME, DATA_TYPE from {self._schema}.COLUMNS where TABLE_NAME = '{table.tableName}'"
            self._cursor.execute(squery)
            res = self._cursor.fetchall()

            # For each field in the result
            for field in res:
                # insert field into the table
                table.insertSchema(field)
            
# Object class to hold table info
class Table(object):
    def __init__(self, name: str, fields: list = None):
        # Create attributes
        self.tableName = name
        self.schema = {}

        # If fields is not undefined, iterate through list with insertSchema
        if fields!=None: [self.insertSchema(i) for i in fields]
    
    # Insert Tuples (<columnName>, <columnType>) into schema (changing the <columnType> if the <columnName> already exists)
    def insertSchema(self, field: tuple):
        self.schema[field[0]] = field[1]