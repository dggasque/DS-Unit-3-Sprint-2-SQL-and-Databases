import pandas as pd
import sqlite3 as sql
import psycopg2 as psy


# Load titanic.csv into a dataframe
df = pd.read_csv('titanic.csv')
df.columns = df.columns.str.replace(" ", "_")
df.columns = df.columns.str.replace("/", "_")
df['Name'] = df['Name'].str.replace("'", " ")


# Create and connect to sqlite3 database
sql_conn = sql.connect('titanic.sqlite3')


# Initiate cursor
sql_curs = sql_conn.cursor()


# Convert dataframe to sql table
df.to_sql('titanic', sql_conn)


# Pull the info from the sqlite table to be converted and loaded into ElephantSQL database
titanic = sql_curs.execute('SELECT * FROM titanic').fetchall()


# Connection settings for ElephantSQL
# Information removed for security
dbname = ''
user = ''
password = ''
host = ''


# Establish connection to PostgreSQL database 
pg_conn = psy.connect(dbname=dbname, user=user, password=password, host=host)


# Initiate cursor
pg_curs = pg_conn.cursor()
pg_curs.execute("CREATE TYPE sex AS ENUM ('male', 'female');")


# Query script to create table
create_titanic_table = """
    CREATE TABLE titanic (
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex sex,
    Age REAL,
    Siblings_Spouses_Aboard INT,
    Parents_Children_Aboard INT,
    Fare Real
    );
    """

# Execute Query Script
pg_curs.execute(create_titanic_table)

# Close Cursor and Commit changes to establish table in database
pg_curs.close()
pg_conn.commit()

# Recconect to the database
pg_conn = psy.connect(dbname=dbname, user=user, password=password, host=host)

# Reinitiate cursor
pg_curs = pg_conn.cursor()

# Insert Rows into table

for row in titanic:
    insert_row = """
        INSERT INTO titanic
        (Survived, Pclass, 
        Name, Sex, Age, 
        Siblings_Spouses_Aboard, 
        Parents_Children_Aboard,Fare)
        VALUES""" + str(row[1:]) + ";"
    pg_curs.execute(insert_row)
    


# Close cursor and commit changes

pg_curs.close()
pg_conn.commit()
