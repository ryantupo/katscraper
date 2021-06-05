import scrapy
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="katsdb"
)

mycursor = db.cursor()

mycursor.execute("SELECT * FROM Images")

rows = mycursor.fetchall()
for i in mycursor:
    print("link :",i)

# def add_image(Link):
#     mycursor.execute(f"INSERT INTO Images (link) VALUES ('{Link}')")
#     print ("sddsfsdfs")
#     mycursor.execute("SELECT * FROM Images")
#     rows = mycursor.fetchall()
#     for i in rows:
#         print (i)


# add_image("https://images-na.ssl-images-amazon.com/Mobile_IT._CR0,240,3000,720_SX1250_.jpg")



#mycursor.execute("CREATE TABLE Images (link VARCHAR(244), imageID int primary key AUTO_INCREMENT)")
# mycursor.execute("CREATE DATABASE katsdb")


