#!/usr/bin/python
import psycopg2
import os
import time

start = time.time()
db_files = {
    'country_vaccinations' : './DATA/country_vaccinations.csv',
}

# Connect to DB
conn = psycopg2.connect(
    database="postgres",
    user='postgres',
    password='postgrespw',
    host='127.0.0.1',
    port= '5432'
)

conn.autocommit = True
cursor = conn.cursor()

try:
    for i in db_files:
            # print(i, db_files[i])
            try:
                with open(db_files[i], 'r') as f :
                    next(f)
                    cursor.copy_from(f, i, sep=',')
            except (Exception, psycopg2.Error) as error:
                print("Error whole loading data: ", error)

except (Exception, psycopg2.Error) as error:
    print("Some Error: ", error)

finally:
    if conn:
        cursor.close()
        conn.close()
        print("connection closed. End.")


print("Total execution time {0:0.3f} seconds".format(time.time() - start))
