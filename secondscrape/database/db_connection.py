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
    mycursor.execute(f"SELECT COUNT(1) FROM images WHERE link ='{url}'")
    
    amount_of_matches = mycursor.fetchall()
    
    list_of_matches = amount_of_matches[0]
    
    if (list_of_matches[0]) > 0:
        return True
    else:
        return False

def check_link(url):
    mycursor.execute(f"SELECT COUNT(1) FROM links WHERE link ='{url}'")
    
    amount_of_matches = mycursor.fetchall()
    
    list_of_matches = amount_of_matches[0]
    
    if (list_of_matches[0]) > 0:
        return True
    else:
        return False
    
def commit_data():
    db.commit()
    print(mycursor.rowcount, "record inserted.")

def add_image(Link):
    if check_url(Link) == False:
        print ("Image Found")
        mycursor.execute(f"INSERT INTO Images (link) VALUES ('{Link}')")
        commit_data()
    else:
        print ("duplicate Image found")   
        
def add_link(Link):
    if check_link(Link) == False:
        print ("Link found")
        mycursor.execute(f"INSERT INTO links (link) VALUES ('{Link}')")
        commit_data()
    else:
        print ("duplicate Link found")   
         
def print_table():
    mycursor.execute("SELECT * FROM Images")
    table = mycursor.fetchall()
    for i in table:
        print (i)

def add_row():
     mycursor.execute("CREATE TABLE links (link VARCHAR(244), linkID int primary key AUTO_INCREMENT)")
    
def log_data(html):
    with open("frontpage.html", "w") as page:
        page.write(html)
        page.close()


    with open("frontpage.json", "w") as page:
        page.write(html)
        page.close()





# add_image("https://images-na.ssl-images-amazon.com/Mobile_IT._CR0,240,3000,720_SX1250_.jpg")


# mycursor.execute("CREATE TABLE links (link VARCHAR(244), linkID int primary key AUTO_INCREMENT)")
#mycursor.execute("CREATE TABLE Images (link VARCHAR(244), imageID int primary key AUTO_INCREMENT)")
# mycursor.execute("CREATE DATABASE katsdb")


