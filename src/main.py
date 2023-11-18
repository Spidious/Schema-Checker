from sqlServer import SQLConnector as sqlconn

if __name__ == "__main__":
    # Create the connector
    conn = sqlconn("INFORMATION_SCHEMA")

    # Fetch the tables and fill their schemas
    conn.fetchTables()
    conn.fetchSchema()

    # Close the connector
    conn.close()
