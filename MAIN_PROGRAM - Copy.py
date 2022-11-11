import mysql.connector as msql
import creation_alpha
from datetime import date
try:
    creation_alpha.database_creation()
    creation_alpha.create_menu()
    creation_alpha.create_studentdetails()
    creation_alpha.create_customerhistory()
    creation_alpha.pwd_creation()
    db=msql.connect(
        host="localhost",
        user="root",
        passwd="marypius",
        database="canteen_alpha")
    mycursor=db.cursor()
except:
    try:
        db=msql.connect(
        host="localhost",
        user="root",
        passwd="marypius",
        database="canteen_alpha")
        mycursor=db.cursor()
    except Exception as err :
        print(err)
        print("Connection failed")
from prettytable import PrettyTable
try:
    def addmenu():
        mycursor.execute('select MAX(Sno) from menu')
        result=mycursor.fetchall()
        i=result[0][0]+1
        n=input('Enter the name of the item :')
        c=int(input('Enter the cost of the item :'))
        table=mycursor.execute("INSERT INTO menu(Sno,Itemname,Price)VALUES({},'{}',{})".format(i,n,c))
        db.commit()
        print("New Item",n,"has been added successfully with Item no:",i,"and cost ",c)         
    def delmenu():
        i=int(input('Enter the item no.to be deleted :'))
        if checkitem1(i)==True:
            mycursor.execute('Delete from menu where Sno={}'.format(i))
            db.commit()
            print("Deletion of the item with S.no",i,"is SUCESSFULL")
        else:
            print('The given Item No. is INVALID')
    def displaymenu():   
        t1=PrettyTable(["SNO","ITEMNAME","PRICE"])
        mycursor.execute('select * from menu')
        for row in mycursor:
            r=list(row)
            t1.add_row(r)
        t1.align["PRICE"] = "r" 
        print(t1)
    def updatemenu():
        displaymenu()
        i=int(input('Enter the item_no to which updation has to be taken place :'))
        if checkitem1(i)==True:
            t1=PrettyTable(["CHOICE","OPERATION"])
            t1.add_row([1,"UPDATE NAME OF ITEM"])
            t1.add_row([2,"UPDATE COST OF ITEM"])
            t1.add_row([3,"UPDATE NAME AND COST OF ITEM"])
            print(t1)
            ch=int(input("Enter your choice"))
            if ch==1:
                n=input('Enter the new name :')
                mycursor.execute("UPDATE menu SET Itemname='{}' where Sno={}".format(n,i))
                db.commit()
                print("NAME OF ITEM No.",i,"IS UPDATED SUCCESSFULLY")
            elif ch==2:
                p=int(input('Enter the new cost :'))
                mycursor.execute("UPDATE menu SET Price={} where Sno={}".format(p,i))
                db.commit()
                print("PRICE OF ITEM No.",i,"IS UPDATED SUCCESSFULLY")
            elif ch==3:               
                n=input('Enter the new name :')
                p=int(input('Enter the new cost :'))
                mycursor.execute("UPDATE menu SET Itemname='{}',Price={} where Sno={}".format(n,p,i))
                db.commit()
                print("DATA OF ITEM No.",i,"UPDATED SUCCESSFULLY")
            else:
                print("PLEASE ENTER THE CORRECT CHOICE")
        else:
            print('The given Item No. is INVALID')
    def checkitem():
        no=int(input("Enter the serial number of the item :"))
        mycursor.execute('SELECT * FROM menu')
        res=mycursor.fetchall()
        found=0
        for i in res:
            if i[0]==no:
                found=1
                print("The item ",i[1]," having item_no: ",i[0]," and cost ",i[2]," is PRESENT in our menu")
                break
        if found==0:
            print('INVALID Serial No.')
            return None
    def checkstud(n):
        mycursor.execute('SELECT * FROM Student_details')
        res=mycursor.fetchall()
        found=0
        for i in res:
            if i[0]==n:
                found=1
                print("The Student Name:",i[1])
                print("Class:",i[2])
                print("Is PRESENT in School database")
                break
        if found==0:
           return None
    def checkitem1(no):
        mycursor.execute('SELECT * FROM menu')
        res=mycursor.fetchall()
        found=0
        for i in res:
            if i[0]==no:
                found=1
                return True
        if found==0:
            return None
    def checkstud1(a):
        mycursor.execute('SELECT * FROM Student_details')
        res=mycursor.fetchall()
        found=0
        for i in res:
            if i[0]==a:
                found=1
                return True
        if found==0:
           return None    
    def bill():
        print("WELCOME TO THE BILLING COUNTER------PLEASE KEEP CHANGE IN HAND")
        print()
        t=PrettyTable(['SLNO','ITEM NO','ITEM NAME','QUANTITY','PRICE','TOTAL'])
        t.align["TOTAL"] = "r"
        t.align["SLNO"] = "c"
        t.align["ITEM NO"] = "c"
        t.align["QUANTITY"] = "c"        
        no=int(input("Input the student's ID_No.:"))
        checkstatus1=checkstud1(no)
        if checkstatus1==True:
            checkstud(no)
            date1=date.today()            
            Total=int(input('Enter the Total no. of items consumed :'))#                          
            mycursor.execute("SELECT MAX(Bill_No) FROM Customer_History")                           
            res1=mycursor.fetchall()
            billnumber=res1[0][0]+1#
            grandtotal=0
            displaymenu()
            print()
            for i in range(Total):
                itemno=int(input("Enter Item_No of the item given in the menu: "))
                checkstatus2=checkitem1(itemno)
                if checkstatus2==True:
                    quantity=int(input("Enter the quantity of the item ordered :"))#
                    mycursor.execute("SELECT Itemname,Price FROM menu WHERE Sno={}".format(itemno))
                    res2=mycursor.fetchall()
                    itemname=res2[0][0]
                    price=res2[0][1]#
                    totalitemcost=price*quantity#
                    grandtotal=grandtotal+totalitemcost##
                    #list for the table
                    rowlist=[i+1,itemno,itemname,quantity,price,totalitemcost]
                    t.add_row(rowlist)
                    print()
                else:
                    print("PLEASE ENTER CORRECT DETAILS ONLY")
                    break
            print()
            print("=========================BILL=============================")
            print()
            print("DATE OF TRANSACTION :",date1)
            print("BILL NUMBER = ",billnumber)
            print()
            mycursor.execute("SELECT Student_name,Class from Student_details where Id_no='{}'".format(no))
            res3=mycursor.fetchone()
            name=res3[0]
            cls=res3[1]
            print("STUDENT NAME :",name)
            print("CLASS:",cls)
            print()
            print(t)
            print()
            print("THE GRANDTOTAL IS = ₹",grandtotal,"/- only")
            print()
            print("PLEASE DO VISIT AGAIN!!")    
        else:
            print("PLEASE TRY AGAIN,STUDENT ID_No. DOES NOT EXIST IN SCHOOL DATABASE")    
        mycursor.execute("INSERT INTO Customer_History(Bill_No,Student_ID,Date,Total_Amount)VALUES({},{},'{}',{})".format(billnumber,no,date1,grandtotal))
        db.commit()
        print()
        print("DATA ENTERED IS SAVED SUCCESSFULLY INTO THE TRANSACTION HISTORY")
        print()        
    def serbill():#VERIFIED
        b=int(input('Enter the bill no :'))
        mycursor.execute('select * from Customer_History where bill_no={}'.format(b))
        res=mycursor.fetchall()
        print("The transaction was done by the student having Id-no",res[0][1],"on",res[0][2])
        print("The total transaction amount was",res[0][3])        
    def allbills():
        t=PrettyTable(["Bill_No","Student_ID","Date","Total_Amount"])
        t.align["Total_Amount"] = "r"
        mycursor.execute("SELECT * FROM Customer_History")
        res=mycursor.fetchall()
        l=len(res)
        for i in range(0,l):
            k=res[i]
            k=list(k)
            t.add_row(k)
        print(t)
    def transacdate():
        d=input('Enter the date(in YYYY-MM-DD format) in which details and no. of transaction done needed:')
        t=PrettyTable(["Bill_No","Student_ID","Date","Total_Amount"])
        t.align["Total_Amount"] = "r"
        mycursor.execute("SELECT * FROM Customer_History where date='{}'".format(d))
        res=mycursor.fetchall()
        l=len(res)
        print("No. of transaction done on",d,"was",l)
        for i in range(0,l):
            k=res[i]
            k=list(k)
            t.add_row(k)
        print(t)        
    def caltotal():
        d=input('Enter the required date(in YYYY-MM-DD format) :')
        mycursor.execute("SELECT SUM(Total_Amount) FROM Customer_History WHERE date='{}'".format(d))
        res=mycursor.fetchall()
        a=res[0][0]
        print("The Total-sales conducted on",d,"was ₹",a,"/-")
    def amtdates():
        d=input('Enter the from date(in YYYY-MM-DD format) :')
        s=input('Enter the to date(in YYYY-MM-DD format) :')
        mycursor.execute("SELECT SUM(Total_Amount) FROM Customer_History WHERE date BETWEEN '{}' and '{}'".format(d,s))
        res=mycursor.fetchall()
        a=res[0][0]
        print("The Total-sales conducted between dates",d,"and",s,"including both dates was ₹",a,"/-")
    def amtstudent():
        i=int(input('Enter the students ID No.'))
        d=input('Enter the from date(in YYYY-MM-DD format) :')
        s=input('Enter the to date(in YYYY-MM-DD format) :')
        mycursor.execute("SELECT SUM(Total_Amount) FROM Customer_History WHERE Student_ID={} and date BETWEEN '{}' and '{}'".format(i,d,s))
        res=mycursor.fetchall()
        a=res[0][0]
        print("The Total_Amount paid by student having ID_No.",i," between dates",d,"and",s,"including both dates was ₹",a,"/-")     
    def pwd_check(a):
        f=open("password.txt","r")
        b=0
        b=f.read()
        if a==b:
            return True
        else:
            return False
    def pwd_creation():
        try:
            fc=open("password.txt","w")
            p1=input("New password :")
            fc.write(p1)
            fc.close()
            print("PASSWORD SUCESSFULLY EDITED")
        except Exception as err:
            print(err)    

###############################################################################################
    while True:
        print("************** WELCOME TO ST:ANTONY'S PUBLIC SCHOOL CANTEEN ******************")
        print("PLEASE ENTER THE CORRECT PASSWORD TO UNLOCK ADMIN PRIVILAGES")
        password=input("ENTER PASSWORD :")
        f=pwd_check(password)
        if f==True:
            print("YOU WILL NOW HAVE ADMINISTRATIVE PRIVILAGES")
            admin=1
        else:
            print("YOU WILL NOW HAVE GUEST PRIVILAGES ONLY")
            admin=0
        print("PLEASE SELECT THE KIND OF OPERATION YOU ARE ABOUT TO PERFORM")
        t1=PrettyTable(["CHOICE","OPERATION"])
        t1.add_row([1,"UPDATION OR MANIPULATION IN DATABASE(ADMIN)"])
        t1.add_row([2,"BILLING"])
        t1.add_row([3,"VIEWING DATA FROM THE DATABASE(ADMIN)"])
        t1.add_row([4,"CHANGING/EDITING THE CURRENT ADMIN PASSWORD(ADMIN)"])
        print(t1)
        ch1=int(input("Enter your choice :"))
        print()
        try:
            if ch1==1 and admin==1:
                while True:
                    print("YOU HAVE OPTED TO EDIT THE DATABSE")
                    print("NOW SELECT THE REQUIRED EDITIVE TASK")
                    t2=PrettyTable(["CHOICE","OPERATION"])
                    t2.add_row([1,"ADD NEW FOOD ITEM INTO MENU"])
                    t2.add_row([2,"UPDATE DETAILS ABOUT AN EXISTING FOOD ITEM"])
                    t2.add_row([3,"DELETE AN EXISTING FOOD ITEM FROM THE MENU"])
                    print(t2)
                    ch2=int(input('Enter your choice :'))                    
                    if ch2==1:
                        addmenu()
                    elif ch2==2:
                        updatemenu()
                    elif ch2==3:
                        delmenu()
                    else:
                        print("***PLEASE ENTER THE CORRECT CHOICE***")
                        print()                        
                    if input('Do you want to continue "MANUPILATION IN THE DATABASE"(Y/N) :').upper()!='Y':
                        break
            elif ch1==2:
                while True:
                    print("YOU CHOOSE TO PROCESS A BILL")
                    print()
                    try:
                        bill()
                    except Exception as err :
                        print(err)
                        print()
                    if input('Do you want to continue billing(Y/N) :').upper()!='Y':
                        break
            elif ch1==3 and admin==1:
                while True:
                    print("YOU CHOOSE FOR DISPLAYING DATA FROM THE DATABASE")
                    t3=PrettyTable(["CHOICE","OPERATION"])
                    t3.add_row([1,"TO DISPLAY THE ORDER MENU"])
                    t3.add_row([2,"TO COLLECT OF A SPECIFIC ITEM IN THE MENU"])
                    t3.add_row([3,"TO COLLECT DETAILS OF A SPECIFIC STUDENT FROM THE DATABASE"])
                    t3.add_row([4,"TO CHECK WHETHER A SPECIFIC ITEM IS PRESENT IN THE MENU OR NOT"])
                    t3.add_row([5,"TO CHECK WHETHER A SPECIFIC STUDENT IS PRESENT IN THE DATABASE OR NOT"])
                    t3.add_row([6,"TO COLLECT DETAILS OF A SPECIFIC PAST TRANSACTION FROM THE DATABASE"])
                    t3.add_row([7,"TO COLLECT THE DETAILS OF ALL THE BILLS AND TRANSACTIONS THAT HAD TAKEN PLACE SO FAR"])
                    t3.add_row([8,"TO COLLECT THE TOTAL AMOUNT OF TRANSACTION THAT HAD TOOK PLACE IN THE GIVEN DATE"])
                    t3.add_row([9,"TO COLLECT THE TOTAL AMOUNT OF TRANSACTION THAT HAD TOOK PLACE IN BETWEEN GIVEN DATES"])
                    t3.add_row([10,"TO COLLECT THE TOTAL AMOUNT OF PAID BY A SPECIFIC STUDENT IN BETWEEN GIVEN DATES"])
                    t3.add_row([11,"TO COLLECT THE DETAILS AND No. OF TRANSACTIONS THAT HAD TAKEN IN THE GIVEN DATE"])
                    t3.align["OPERATION"]="l"
                    print(t3)
                    ch3=int(input('Enter your choice :'))
                    if ch3==1:
                        displaymenu()
                    elif ch3==2:
                        checkitem()
                    elif ch3==3:
                        b=int(input("ENTER THE STUDENT'S ID_No. :"))
                        checkstud(b)
                    elif ch3==4:
                        a=int(input("ENTER THE ITEM NUMBER OF THE REQUIRED ITEM FROM MENU :"))
                        print(checkitem1(a))
                    elif ch3==5:
                        b=int(input("ENTER THE STUDENT'S ID_No. :"))
                        print(checkstud1(b))
                    elif ch3==6:
                        serbill()
                    elif ch3==7:
                        allbills()
                    elif ch3==8:
                        caltotal()
                    elif ch3==9:
                        amtdates()
                    elif ch3==10:
                        amtstudent()
                    elif ch3==11:
                        transacdate()
                    else:
                        print("***PLEASE ENTER THE CORRECT CHOICE***")                    
                    if input('Do you want to continue "DISPLAYING DATA FROM THE DATABASE"(Y/N) :').upper()!='Y':                            
                        break                
            elif ch1==4 and admin==1:
                pwd_creation()
            elif admin==0 and ch1!=2:
                print("Sorry, INVALID OPERATION and you are only a GUEST USER")    
            else:
                 print("***PLEASE ENTER THE CORRECT CHOICE***")
        except:
            print("***PLEASE ENTER THE CORRECT CHOICE***")
        if input("Would you like to work more with the databse??(Y/N) :").upper()!='Y':
            break 
except Exception as err:
    print(err)
print()
print("THANK YOU FOR VISITING PLEASE COME AGAIN")
print()
print("ALL CREDITS AND COPYRIGHTS GOES TO ADZ,MYTH,AJP")
#Done by Alex and Adithyan
#Debugged by Adithyan


