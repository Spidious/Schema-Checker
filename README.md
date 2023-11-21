# Schema Checker

Excel file name should be "schemaname_email.xlsx"
i.e.: 'userdb_example@example.com.xlsx'

Checks an Excel file to see if matches a table schema in a SQL Server database.

- Activate your [python venv](https://docs.python.org/3/library/venv.html) and install the requirements.txt with
  `pip install -r requirements.txt`
- In `config/server.yaml` fill in the correct info
- Change the EXCEL variable in `main.py`
