# NoSQL and Document-oriented databases

NoSQL, no worries? Not exactly, but it's still a powerful approach for some
problems.

## Learning Objectives

- Identify appropriate use cases for document-oriented databases
- Deploy and use a simple MongoDB instance

## Before Lecture

Sign up for an account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas),
the official hosted service of MongoDB with a generous (500mb) free tier. You
can also explore the many [MongoDB tools](http://mongodb-tools.com/) out there,
though none in particular are recommended or required for installation (we're
really just checking out MongoDB as a way to understand document-oriented
databases - it's unlikely to become a core part of your toolkit the way SQLite
and PostgreSQL may).

## Live Lecture Task

Another database, same data? Let's try to store the RPG data in our MongoDB
instance, and learn about the advantages and disadvantages of the NoSQL paradigm
in the process. We will depend on
[PyMongo](https://api.mongodb.com/python/current/) to connect to the database.

Note - the
[JSON](https://github.com/LambdaSchool/Django-RPG/blob/master/testdata.json)
representation of the data is likely to be particularly useful for this purpose.

## Assignment

Reproduce (debugging as needed) the live lecture task of setting up and
inserting the RPG data into a MongoDB instance, and add the code you write to do
so here. Then answer the following question (can be a comment in the top of your
code or in Markdown) - "How was working with MongoDB different from working with
PostgreSQL? What was easier, and what was harder?"

There is no other required tasks to turn in, but it is suggested to then revisit
the first two modules, rework/complete things as needed, and just check out with
fresh eyes the SQL approach. Compare and contrast, and come with questions
tomorrow - the main topic will be database differences and tradeoffs!
```python
"""
It was more difficult to succesfully establish a connection to the MongoDB, but much easier to maintain the connection as mistakes did not break it. It is easier to conceptualize the PostgreSQL database, because of the relational connections between tables. I am already familiar with SQL queries, so interacting with the data is much easier.  
"""
import pymongo
import sqlite3

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0-6pbrr.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

def write_to_mongo(tables, cursor, mongodb):
    """
    Takes tables from sglite3 database and writes the data
    in the tables to Mongodb 
    """
    tables = get_names(tables)
    for table in tables:
        columns = get_columns(cursor, table)
        data = get_table_data(cursor, table)
        for row in data:
            doc = {}
            for i in range(len(row)):
                doc.update({columns[i]: row[i]})
            mongodb.test.insert_one(doc)


def get_names(tables):
    """
    Pulls table names from Tuples in the tables list
    """
    table_names = []
    for table in tables:
        table_names.append(table[0])
    return table_names

def get_columns(cursor, table_names):
    """ 
    Takes table names and returns list of columns
    in the table
    """
    table_info = curs.execute(f'PRAGMA table_info({table});').fetchall()
    columns = []
    for info in table_info:
        columns.append(info[1])
    return columns

def get_table_data(cursor, table):
    """
    Returns row data for table
    """
    return curs.execute(f'SELECT * FROM {table}').fetchall()

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

write_to_mongo(tables, curs, db)
```
## Resources and Stretch Goals

Put Titanic data in Big Data! That is, try to load `titanic.csv` from yesterday
into your MongoDB cluster.

Push MongoDB - it is flexible and can support fast iteration. Design your own
database to save some key/value pairs for an application you'd like to work on
or data you'd like to analyze, and build it out as much as you can!
