import sqlite3

con = sqlite3.connect("favorites.db")
print("Database opened successfully")

con.execute(
    "create table Favorites (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, fav_minecraft_mob TEXT NOT NULL, fav_football_team TEXT NOT NULL, fav_food TEXT NOT NULL, fav_car TEXT NOT NULL)")


print("Table created successfully")

con.close()