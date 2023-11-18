from sqlServer import SQLConnector, Table
from xlReader import xlsxParser

if __name__ == "__main__":
    # Create the connector
    conn = SQLConnector("INFORMATION_SCHEMA")

    # Fetch the tables and fill their schemas
    conn.fetchTables()
    conn.fetchSchema()

    # Close the connector
    conn.close()

    # Parse the excel file
    xp = xlsxParser("placeholder.xlsx")

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

    # Raise exception since the headers don't match.
    if match == "":
        raise Exception("No matching schema was found: Check you headers")






