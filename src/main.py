from sqlServer import SQLConnector as sqc

if __name__ == "__main__":
    conn = sqc("INFORMATION_SCHEMA")
    conn.fetchTables()
    for table in conn.tables: print(table.tableName)
    conn.close()
