import sqlite3

# Example query to PUT data
# INSERT INTO events(DB Name) VALUES ('Tigers', 'Tiger City', '2088.10.14')

# Example query to QUERY data
# SELECT * FROM events WHERE date(DB Column)='2088.10.14'

# Example query to DELETE data
# DELETE FROM events WHERE band='Tigers'


# Establish Connection & Cursor
connection = sqlite3.connect("data_sql_lite.db")
cursor = connection.cursor()


# # Query all Data based on a condition
# cursor.execute("SELECT * FROM events WHERE band='Lions'")
# print(cursor.fetchall())

# # Query certain columns based on a condition
# cursor.execute("SELECT band, date FROM events WHERE date='2030.10.15'")
# print(cursor.fetchall())

# # Insert new rows 
# new_db_rows = [('Cats', 'Liverpool', '2030.10.17'),
#                 ('Sheep', 'Swansea', '2024.07.15')]

# cursor.executemany("INSERT INTO events Values(?,?,?)", new_db_rows)
# ## Write changes
# connection.commit()

# Query all the data
cursor.execute("SELECT * FROM events")
print(cursor.fetchall())