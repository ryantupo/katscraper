import scrapy
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="katsdb"
)

mycursor = db.cursor()

def check_url(url):
    print ("sdinhfsfjsdnbfljnsbdljfnbsdjolfnbsdojnbfsdnfosdjnbfojsdbnfojksdnbfojklsdnfljk")
    mycursor.execute(f"SELECT COUNT(1) FROM images WHERE link ='{url}'")
    amount_of_matches = mycursor.fetchall()
    
    print ("the amount of matches ????" , amount_of_matches)
    if len(amount_of_matches) > 0:
        return True
    else:
        return False
    


def commit_data():
    db.commit()
    print(mycursor.rowcount, "record inserted.")

def add_image(Link):
    if check_url(Link) == False:
        print ("WE GOT AN IMAGE BABY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        mycursor.execute(f"INSERT INTO Images (link) VALUES ('{Link}')")
        commit_data()
    else:
        print ("duplicate")    
def print_table():
    mycursor.execute("SELECT * FROM Images")
    table = mycursor.fetchall()
    for i in table:
        print (i)

# add_image("https://images-na.ssl-images-amazon.com/Mobile_IT._CR0,240,3000,720_SX1250_.jpg")



#mycursor.execute("CREATE TABLE Images (link VARCHAR(244), imageID int primary key AUTO_INCREMENT)")
# mycursor.execute("CREATE DATABASE katsdb")


