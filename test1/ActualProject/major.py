import pandas as pd
import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user='root',
    password='Thejocker21',
    database='userprofile'
)

try:
    cursor = connection.cursor()

    # Define the path to the Excel file
    excel_file_path = 'Copy_of_Major_File.xlsx'

    # Create a list of row indices to skip
    skips = [i for i in range(2, 95, 2)]

    # Read the Excel file, skipping specified rows and using only the 5th column
    df = pd.read_excel(excel_file_path, skiprows=skips, usecols=[5], nrows=92)
    df.columns = ['major']
    print(df)

    # Replace NaN values with a default value (e.g., "N/A")
    df['major'].fillna('N/A', inplace=True)

    # Create the 'major_table' SQL table
    major_table_sql = """
    CREATE TABLE IF NOT EXISTS major_table (
        major VARCHAR(50)
    )
    """

    cursor.execute(major_table_sql)

    # Insert data from the DataFrame into the SQL table
    insert_query = "INSERT INTO major_table (major) VALUES (%s)"
    for _, row in df.iterrows():
        cursor.execute(insert_query, (row['major'],))

     # Define the SQL statement to add the 'status' column
    add_status_column_sql = """
    ALTER TABLE requesttable
    ADD COLUMN status VARCHAR(50)
    """

    # Execute the SQL statement to add the 'status' column
    cursor.execute(add_status_column_sql)

    # Commit the changes
    connection.commit()

    print("Column 'status' added to 'requesttable' successfully!")


finally:
    # Close cursor and connection
    cursor.close()
    connection.close()
