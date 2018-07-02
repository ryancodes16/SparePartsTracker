import sqlite3
import time
import datetime
import random
import webbrowser


conn = sqlite3.connect('Part.db')
c = conn.cursor()

def driver():
      create_table()
      print ("Welcome to the Epiq Spare Parts tracking application!")
      print ("For any needed updates or help email rregier@epiq-solutions.com")
      #time.sleep(5)
      print ("The following code run will be demo code to showcase how the Spare Parts Tracker is light-weight yet powerful and useful.")
      #time.sleep(5)
      for i in range(5):
               print(" ")
      part_entry();
      for i in range(5):
               print(" ")
      part_search();
      for i in range(5):
               print(" ")
      delete_parts()
    

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS PartDB(datestamp TEXT, Part TEXT, Quantity REAL, Location TEXT)")

def data_entry():
    c.execute("INSERT INTO PartDB VALUES('2018-06-30','Capacitor 2',3, 'Box:5, Shelf: 10')")
    conn.commit()

def dynamic_data_entry():
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    Part = 'Resistor'
    Quantity = random.randrange(0,10)
    Location = 'Shelf: ' + str(random.randrange(1,10)) + ' Box: ' + str(random.randrange(1,10))
    c.execute("INSERT INTO PartDB (datestamp, Part, Quantity, Location) VALUES (?, ?, ?, ?)",
              (date, Part, Quantity, Location)) 


    conn.commit()
    
def part_entry(): #manually insert stuff or use scanner
    cont = True
    while (cont == True):
        unix = int(time.time())
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        print ("Enter the quantity below:[integer]")
        quantity = input();
        print ("Enter the location below:")
        print ("Enter the shelf number below:")
        shelf = input()
        print ("Enter the box below:")
        box = input()
        location = 'Shelf:' + str(shelf) + '| Box: ' + str(box)
        print ("Scan the part barcode or manually type it in below:")
        part = input()
        c.execute("INSERT INTO PartDB (datestamp, Part, Quantity, Location) VALUES (?, ?, ?, ?)",
              (date, part, quantity, location))
        conn.commit()
        print (part, " was entered in correctly and is now available in the database!")
        print ("Continue scanning in more parts? [y/n]")
        response = input()
        if(response == "y"):
            cont = True
        else:
            cont = False
            print ("Have a nice life :)")
            #webbrowser.open('http://epiqsolutions.com')


def part_search(): #search if a part is in stock
    print("Would you like to see all available parts or do a priority search? [ALL/PRIORITY]")
    answer = input()
    if (answer == "ALL"):
         select_all_tasks()
         for i in range(5):
             print(" ")
    elif (answer == "PRIORITY" ):
        print ("If no parts are shown during the priority search, then there are no parts of that type in stock or correctly entered into the database.")
        print ("Enter the priority part below:")
        priority = input()
        select_priority(priority)
        
def select_all_tasks():
    c.execute("SELECT * FROM PartDB")
    rows = c.fetchall()
    for row in rows:
        print(row)
        
def select_priority(priority):
    c.execute("SELECT * FROM PartDB WHERE Part=?", (priority,))
    rows = c.fetchall()
    for row in rows:
        print(row)

def delete_parts():
    cont = True
    while (cont == True):
        print ("Enter the serial number of the part you would like to delete from the database")
        delete = input()
        c.execute("SELECT * FROM PartDB")
        ##  c.execute("UPDATE PartDB SET Part = '99' where Part = '12345'")
        c.execute("DELETE FROM PartDB WHERE Part=?", (delete,))
        #c.execute('DELETE FROM PartDB WHERE Part = 12345')
        conn.commit()
        print("Successfully executed!")
        print ("Continue deleting more parts? [y/n]")
        response = input()
        if(response == "y"):
            cont = True
        else:
            cont = False
            print ("Have a nice life :)")
def clear_database():
    c.execute("SELECT * FROM PartDB")
    c.execute("DELETE * FROM PartDB")
    conn.commit()
    print ("Database cleared. All previous data is deleted")
    
    
#create_table()
driver()
#part_entry()
#part_search()
#data_entry()
#for i in range(10):
    #dynamic_data_entry()
    #time.sleep(1)


#closing neccessary cursor and communicator with database
c.close()
conn.close()
