# Schema Checker

*so far this will only check if the headers match and find the schema associated*

Checks an Excel file to see if matches a table schema in a SQL Server database.

Will then check if each the values in the following column are the correct type

- Activate your [python venv](https://docs.python.org/3/library/venv.html) and install the requirements.txt with
  `pip install -r requirements.txt`
- In `config/server.yaml` fill in the correct info
- Change the SCHEMA and EXCEL variables in `main.py`

### Resources

[Data type mapping between Python and SQL](https://learn.microsoft.com/en-us/sql/machine-learning/python/python-libraries-and-data-types?view=sql-server-ver16)
