import mysql.connector as msql
db=msql.connect(
        host="localhost",
        user="root",
        passwd="marypius")
mycursor=db.cursor()
def database_creation():
    mycursor.execute("CREATE database canteen_alpha")
    mycursor.execute("USE canteen_alpha")
    print("DATABASE SUCCESSFULL")
    print()
    print()
        
def create_menu():
    try:
        mycursor.execute("CREATE TABLE menu(Sno integer primary key,Itemname varchar(45),Price float(10,3))")
        insertquery="INSERT INTO menu(Sno,Itemname,Price)VALUES(%s,%s,%s)"
        items=[(1,'Tea',10.00),(2,'Coffee',15.00),(3,'plain dosa',7.00),(4,'Masala Dosa',50.00),\
               (5,'Chicken Biriyani',140.00),(6,'Beef Biriyani',110.00),(7,'Veg Biriyani',80.00),\
               (8,'Fish Biriyani',160.00),(9,'Meals(veg)',50.00),(10,'Chicken fried rice',130.00),\
               (11,'Veg fried rice',100.00),(12,'Chicken noodles',130.00),(13,'Veg noodles',100.00),\
               (14,'Ghee rice',60.00),(15,'Fish fry',90.00),(16,'Chicken 65',120.00),\
               (17,'Chicken lollipop',40.00),(18,'Butter chicken',160.00),(19,'Ginger chicken',150.00),\
               (20,'Malabar chicken curry',150.00),(21,'Chicken tandoori(full)',290.00),\
               (22,'Beef fry',120.00),(23,'Beef roast',120.00),(24,'Mutton kuruma',210.00),\
               (25,'mutton stew',200.00),(26,'Egg curry',60.00),(27,'Paneer butter masala',110.00),\
               (28,'Palak paneer',120.00),(29,'Paneer tikka masala',120.00),(30,'tomato curry',80.00),\
               (31,'Cauliflower manchurian',90.00),(32,'Cauliflower dry fry',90.00),\
               (33,'Mushroom masala',90.00),(34,'Vegetable stir fry',140.00),(35,'Naan(plain)',12.00),\
               (36,'Butter naan',15.00),(37,'Chapatti',6.00),(38,'Porotta',10.00),\
               (39,'Porotta(wheat)',12.00),(40,'Omelette',12.00),(41,'Chicken sandwich',40.00),\
               (42,'Veg sandwich',25.00),(43,'Samosa',10.00),(44,'Chicken cutlet',10.00),\
               (45,'Veg cutlet',8.00),(46,'Fresh juice',30.00),(47,'Lime juice',10.00),\
               (48,'Lime soda',20.00),(49,'Frooti',20.00),(50,'Mineral Water(1Ltr)',15.00)]
        table1=mycursor.executemany(insertquery,items)
        db.commit()
        print()
        print('MENU TABLE SUCESSFULLY CREATED')
        print()
        print()
    except Exception as err1:
        print('Sorry,the following error occured while inserting data:',err1)
def create_studentdetails():
    try:
        mycursor.execute("CREATE TABLE Student_details(Id_no integer primary key,Student_name varchar(60),\
                          Class varchar(20))")
        insertquery="INSERT INTO Student_details(Id_no,Student_name,Class)VALUES(%s,%s,%s)"
        items=[(1001,'Felix K',12),(1002,'Q Abraam',11),(1003,'Akhil Suresh',12),(1004,'Fahad Faisal',11),\
               (1005,'Amith Prasad',10),(1006,'Ankith Sharma',9),(1007,'Michael Stephen',9),\
               (1008,'M Jackson',11),(1009,'S Raina',12),(1010,'Virat Sharma',10),(1011,'Tony S',11),\
               (1012,'Steve Rogers',12),(1013,'Bruce B',10),(1014,'Leo M',12),(1015,'Jimmy Donaldson',12),\
               (1016,'Hasan Ali',11),(1017,'Khaleel Ahmed',9),(1018,'Sreyas Sharma',10),\
               (1019,'Isaac N',12),(1020,'Albert E',10),(1021,'Vinod Kumar',11),(1022,'Abhinav Hari',11),\
               (1023,'Paul Harris',11),(1024,'Dheeraj Singh',9),(1025,'Vishal R',12),\
               (1026,'Vineeth Mohan',10),(1027,'Ahmad Khan',10),(1028,'Deepak K',9),\
               (1029,'Alex Joseph Pius',12),(1030,'Adithyan V',12),(1031,'Mithun S Anil',12),\
               (1032,'Vijay s',10),(1033,'Chris Watson',11),(1034,'Saleel Mohammed',11),\
               (1035,'Kobe B',12),(1036,'M Raja',12),(1037,'Patrick Carney',9),(1038,'Chandler B',12),\
               (1039,'Karl Jacobs',9),(1040,'Zaid Malik',9),(1041,'Aarush S',10),(1042,'Robert D',12),\
               (1043,'Kevin James',12),(1044,'Mark Rober',10),(1045,'Benjamin Lewis',10),\
               (1046,'Luke W',12),(1047,'Frankiln Thomas',10),(1048,'Ullas R',9),(1049,'Sanjay Singh',10),\
               (1050,'Ryan Reynolds',10)]
        mycursor.executemany(insertquery,items)
        db.commit()
        print()
        print("STUDENT DETAILS SUCCESSFULLY CREATED")
        print()
        print()
    except Exception as err2:
        print('Sorry,the following error occured while inserting data:',err2)
def create_customerhistory():
    try:
        mycursor.execute("create table Customer_History(Bill_No integer unique,\
                          Student_ID integer,Date date,Total_Amount float(20,5))")
        mycursor.execute("INSERT ignore INTO Customer_History VALUES(0,0,'0000-00-00',0)")
        db.commit()
        print()
        print("CUSTOMER HISTORY TABLE SUCCESSFULLY CREATED")
        print()
        print()
    except Exception as err3:
        print('Sorry, the following error occurred:',err3)
def pwd_creation():
        try:
            fc=open("password.txt","w")
            p1=input("New password :")
            fc.write(p1)
            fc.close()
            print("PASSWORD SUCESSFULLY CREATED")
        except Exception as err:
            print(err)
            
#Done by Mithun S Anil
#Debugged by Adithyan.V
