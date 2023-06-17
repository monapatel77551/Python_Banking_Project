

from curses.ascii import isalpha
SpecialList =['$', '@', '#', '%']

#------------Mysql Connection code--------------------------------------------

import mysql.connector
# This is mysql connector to connect mysql server
#mydb = mysql.connector.connect(
   # host="localhost",
    #user="root", 
    #password="mona",
    #db="Banking_Project"
    
    # )
# Cursor objects interact with the MySQL server using a MySQLConnection object
#mydb is a mysql connection object

#mycursor = mydb.cursor()
#mycursor.execute("select * from my table")

#---------------------------------------------------------------------------------


def remove(str):
    # This Method is for removing all space from string  
    # to do that  i have used .replace method 
    return str.replace(" ", "")
while True:
    print("\n")
    print("\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\'''''''''''''''''''''''''''''''''''''''''''")

    print("********************  Welcome To Banking system  *************************")
  
    print("\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"''''''''''''''''''''''''''''''''''''''''''")

    print("\n")
    print("Press 1 For Registration ")
    print("Press 2 For Log In  ")
    print("Press 3 For Exit  ")

    try:
        ch=int(input("Enter the Key : "))
        if(isalpha(ch)) or (ch>=4) or (ch<1) :
            raise Exception ("Oops!  Please enter the valid number.  Try again...  :( ")
        
        #this condition  if true then process is for registration or signup for new user

        elif(ch==1):
            while True:
                try: 
                    ut1 = input("Enter Your Name Here!! : ")
                    ut2 = ut1.strip()
                    ut = remove(ut1)
                    if ut.isalpha() :
                        break
                    else:
                        raise TypeError 
                except TypeError:
                    print("Name should start from charaters not special charactor or word . , @ # < > ? / ; ")

            while True:        
                try:

                    z=input("Enter Your Password : ")
                    if (len(z)<6):
                        raise ValueError (" Password should contain at least 6 character ")
                    if not any(char.isdigit() for char in z):
                        raise ValueError ("Password should atleast a number")
                    if not any(char.isupper() for char in z):
                        raise KeyError ()
                    if not any(char.islower() for char in z):
                        raise KeyError
                    if not any(char in SpecialList for char in z ):
                        raise KeyError
                    break
                except ValueError:
                    print("password should contain  upper-lower-specail and number")
                    print("password should contain upper-lower-special and number length should be atleast 7")
            while True:
                try:
                    try:
                        k=int(input("Enter the Amount of money you want to deposit : "))
                    except:
                        print("Please Enter the value ! \U0001F642 ")
                    if (k<0) :
                        print('\n')
                        print("Amount less than Zero is not exist in the real world only you can think! \U0001F642 ")
                        print('\n') 
                    else:
                        break              
                except:
                    print("Please write correct value !")

            s=input("Enter Your Address : ")

            while True:
                try:
                    d=input("Enter Your Phone Number : ")
                    if (len(d)!=10) or (d.isalpha()):
                        raise ValueError("Pls enter a valid 10 digit Number")
                    break
                except ValueError as m:
                    print(m)
            while True:
                try:
                    f=input("Please enter 12 digit adhar number wihtout space  : ")
                    if(len(f)!=12) or (f.isalpha()):
                        raise ValueError ("Please Enter a valid 12 digit aadhar Number")
                    break
                except ValueError as m:
                    print(m)


# |--------------Here all sql query part will come so that after 
# |------------- register data can be insterted into database-----
# |
        elif(ch==2):
            while True:
                try:
                    u=input("Enter Your name : ")
                    p=input("Enter Your Password : ")
                      
#-------------retrieving data from sql database ---------
                      


                except:
                    print("Enter details are invalid !.Please try again")
        






        elif(ch==3):
            print("Thank You For Visiting! ")
            break

    except Exception:
        print("\n")
        print("Oops! Something went wrong ")
        print("_________________________________________________")
        print("\n")
        break