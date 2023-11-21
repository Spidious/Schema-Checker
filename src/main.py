from sqlServer import SQLConnector
from xlReader import xlsxParser

EXCEL = "userdb_example@gmail.com.xlsx"

# Determines if two lists contain the exact same values
# Requires same number values and the same text values. Does NOT require same order 
def searchLists(xl: list, sql: list) -> bool:
    # Determine if they containt the same number values
    if len(xl) != len(sql): return False
    
    # Determine if they each contain the same values
    for item in xl:
        if sql.count(item) == 0: return False

    return True





if __name__ == "__main__":
    # Open the excel file and get the schema from sql
    file = xlsxParser(EXCEL)
    xlList = file.get_headers()
    sql = SQLConnector()
    sqlList = sql.fetchSchema(file.name)

    # Check each list and then check the values
    if searchLists(xlList, sqlList):
        pass # TODO: Write the value check
        

