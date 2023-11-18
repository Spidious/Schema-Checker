from sqlServer import SQLConnector
from xlReader import xlsxParser

SCHEMA = "INFORMATION_SCHEMA"
EXCEL = "placeholder.xlsx"

if __name__ == "__main__":
    # Create the connector
    conn = SQLConnector(SCHEMA)

    # Fetch the tables and fill their schemas
    conn.fetchTables()
    conn.fetchSchema()

    # Close the connector
    conn.close()

    # Parse the excel file
    xp = xlsxParser(EXCEL)

    # Get the headers from sql server and excel
    xlheaders = xp.get_headers()
    sqlheaders = conn.get_headers()

    # check if the headers have a match
    match = ""
    for key in sqlheaders.keys():
        # first check if they are even the same length
        if len(sqlheaders[key]) != len(xlheaders): continue
        # check if they contain the same headers
        case = True
        # for every index of both lists, if they do not match, switch the case to false and break
        for i in range(0, len(xlheaders)):
            if sqlheaders[key][i] != xlheaders[i]:
                case = False
                break
        # determine if there was a pass or fail
        if not case: break
        else: match = key
        
    # retrieve the matching table
    table = conn.get_table(match)
    # Raise exception since the headers don't match.
    if match == "":
        raise Exception("No matching schema was found: Check you headers")






