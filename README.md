# Canteen-Management-System-In-Python

<h6>The Analysis and retrieval of data are very essential for the success of any organization. Being
 in a competitive world it is not at all easy to follow traditional methods to win the minds of the
 people. The need for innovative ideas to attract users are needed to be implemented so as to flourish in the current scenario. Taking this as the objective I created a management system for a school canteen. The School Canteen management System helps for making necessary updates and analyze the needs of the customer and in turn making more profit.This program is mainly intended for the various activities that are carried out at a School Canteen.It has the provisions to print the bill and to view data as per the need of the User. It is designed in such a way that it can be used with minimum prerequisites.It is developed for the use of the cashier of the canteen.It mainly contains three tables which are menu, customer history and student details.<h6/>
  
  
  
 This projected is mainly divided into 3 python modules
 1) FRAMEWORK
 This module includes the creation of tables and its contents in MySQL using “mysql.connector”
 module.
 It creates mainly 3 tables under a single data base “CANTEEN”. (This contains more tables
 also.)
 This table contains the life-time history of transactions in the school canteen. It contains 3
 columns namely: -
 --Transaction ID
 --Date of transaction
 --Student ID of the student (Primary,ForeignKey)
 --Total sum paid by the student.
 This table contains the information about the food items that are available for serving in the
 canteen on any given day.
 It contains columns namely: -
 -- Item number (Primary,Foreign Key)
 -- Name of the item
 -- Cost of the item
 It contains:-
 --Student ID of the student
 --Student Name
 --Class Name
 --Remarks
BRIEF EXPLANATION
 1.1) HISTORY Table
 1.2) MENU/ITEMS Table
 1.3) STUDENT INFORMATONTable 
 
2) PROCESSING
This module basically contains mainly different functions intended for various
purposes in the table.
2.1) Addition of new item in the menu
2.2) Deletion of an existing item in the menu
2.3) Displaying the items name and number in the menu
2.4) Displaying the number of students who have eaten from the canteen
2.5) Checking whether a specific child has eaten from the canteen
2.6) Displaying the total amount collected from the student
2.7) Updating the price and related details of the items
2.8) Searching for a given product is there in the menu list
2.9) Calculation of total income per day
  3) DISPLAY
 Selling An Item From The Canteen: On entering the Student Id and the Item Number and
 Quantity of each item, the total amount will be calculated and displayed as bill. This amount,
 along with date of the transaction, student id will be added to the History Table as a new row.
