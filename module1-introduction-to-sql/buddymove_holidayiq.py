import sqlite3
import pandas as pd

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

df = pd.read_csv('buddymove_holidayiq.csv')
df.columns = df.columns.str.replace(" ", "_")

curs = conn.cursor()

curs.execute('DROP TABLE review;')

df.to_sql('review', conn)

q1 = 'SELECT COUNT(*) FROM review'

rows = curs.execute(q1).fetchall()

print(f'There are {rows[0][0]} rows in the review table')

q2 = """
     SELECT COUNT(User_Id)
     FROM review
     WHERE Nature >= 100
     AND Shopping >= 100;
     """

result = curs.execute(q2).fetchall()

print(f'There are {result[0][0]} users that have at least 100 Nature and 100 Shopping reviews')