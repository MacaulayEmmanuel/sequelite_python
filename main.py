import sqlite3

connection = sqlite3.connect("tormar_studios.db")
cursor = connection.cursor()

cursor.execute("create table tormar_studios (madeYear integer, warriorName text, city text)")

trajectory_point_list = [
    (1848, "Banabas Olugbogi", "Ondo state"),
    (1999, "Olubgogi Isaac", "Sango otta, Nigeria"),
    (2001, "Nathaniel Olugbogi", "City of Peace"),
    (2002, "Lod Nael: Libertiy City", "Liberty City"),
    (2004, "Macaulay Emmanuel: Freedom State", "State of The Free"),
    (2008, "Akolawole Mathew", "Liberty City"),
    (2013, "Favour Ajayi", "Kansas City")
]    

cursor.executemany("insert into tormar_studios values (?,?,?)", trajectory_point_list)

#printing all the roll in our created database
for row in cursor.execute("select * from tormar_studios"):
    print(row)

#print specific rows
print("____________________________________________________")
cursor.execute("select * from tormar_studios where city=:c", {"c": "Liberty City"})
tStudios_search = cursor.fetchall()
print(tStudios_search)


connection.close()

