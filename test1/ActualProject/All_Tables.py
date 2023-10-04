import pandas as pd
import numpy as np
import mysql.connector


connection = mysql.connector.connect(
    host= "localhost",
    user= 'root',
    password= 'Thejocker21',
    database= 'userprofile' 
)


cursor = connection.cursor()


sign_up_pages_user_sql = """
CREATE TABLE sign_up_pages_user (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    First_Name VARCHAR(255),
    Last_Name VARCHAR(255),
    GPA DOUBLE,
    Major VARCHAR(255),
    Email VARCHAR(255),
    password VARCHAR(255),
    PhoneNumber INT,
    Photo BLOB,
    Gender VARCHAR(255)
)
"""
excel_file_path = 'AUB_Courses.xlsx'


df = pd.read_excel(excel_file_path, skiprows=1, usecols=[2, 3, 17], nrows=352)


df.columns = ['department', 'number', 'instructor']


df['course_id'] = np.arange(1, len(df) + 1)

course_table_sql = """
CREATE TABLE Course_Table (
    course_id INT PRIMARY KEY,
    department VARCHAR(255),
    number VARCHAR(255),
    instructor VARCHAR(255)
)
"""

feedtable_sql = """
CREATE TABLE feedtable (
    Feed_ID INT PRIMARY KEY AUTO_INCREMENT,
    Feed_Owner INT,
    Location VARCHAR(255),
    Description VARCHAR(255),
    Knowledge INT,
    Course INT,
    FOREIGN KEY (Feed_Owner) REFERENCES sign_up_pages_user(ID),
    FOREIGN KEY (Course) REFERENCES course_Table(course_id)
)
"""

requesttable_sql = """
CREATE TABLE requesttable (
    Requesting INT,
    Owner INT,
    Feed INT,
    Course INT,
    PRIMARY KEY (Requesting, Owner, Feed),
    FOREIGN KEY (Requesting) REFERENCES sign_up_pages_user(ID),
    FOREIGN KEY (Owner) REFERENCES sign_up_pages_user(ID),
    FOREIGN KEY (Feed) REFERENCES FeedTable(Feed_ID),
    FOREIGN KEY (Course) REFERENCES course_Table(course_id)
)
"""

# Execute the SQL statements to create the tables
cursor.execute(sign_up_pages_user_sql)
cursor.execute(course_table_sql)
cursor.execute(feedtable_sql)
cursor.execute(requesttable_sql)

# Commit the changes and close the cursor and connection
connection.commit()


insert_query = "INSERT INTO course_table (course_id, department, number, instructor) VALUES (%s, %s, %s, %s)"
for _, row in df.iterrows():
     cursor.execute(insert_query, (row['course_id'], row['department'], row['number'], row['instructor']))

connection.commit()

cursor.close()
connection.close()


print("Tables created successfully!")