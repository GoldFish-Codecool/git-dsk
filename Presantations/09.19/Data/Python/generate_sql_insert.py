import pandas as pd


def generate_sql_insert_statements_from_csv(file_path, stock_id):
    # Load the provided CSV into a pandas DataFrame
    data = pd.read_csv(file_path)

    # Generate the insert statements from the DataFrame
    insert_statements = []
    for index, row in data.iterrows():
        insert_statements.append(
            f"({stock_id}, '{row['Date']}', {row['Open']}, {row['Close']}, {int(row['Volume'])})")

    # Create the SQL insert start command
    sql_insert_start = "INSERT INTO HistoricalData (stock_id, date, opening_price, closing_price, volume) VALUES"

    # Join the insert statements to create the full SQL command
    sql_insert_values = ",\n".join(insert_statements)
    sql_insert_command = sql_insert_start + "\n" + sql_insert_values + ";"

    return sql_insert_command


sql_command = generate_sql_insert_statements_from_csv('AAPL.csv', 'AAPL')
print(sql_command)
