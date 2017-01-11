
## @authors 
    # 1 Sagar Gupta
    # 2 Dhairya Gandhi

## @ smartcampus

## process is like 
    # 1 add ur id on numpad
    # 2 order food
    # 3 uncle enters the amt through another numpad ****
    # 4 us conf the amt by placing finger 
    # 5 screen displays the transaction failed or approved 

## hardware req 
    # 1 raspberry pi
    # 2 finger pirnt module 
    # 3 uart
    # 4 numpad
    # 4 numpad (uncle side) **
    # 5 screen 
    # 6 jumper wires 
    # 7 wifi router 

## backend server is su server 

## script to map the harware and database part 
## script to map server and pi databases
## 

import MySQLdb
import sys
import os

class database:
    def __init__(self,usID='sagar', pswd='toor@123', dbase='IR_assign', hst='localhost'):
        self.userID = usID
        self.password = pswd
        self.database = dbase
        self.host = hst
        try:
            self.db = MySQLdb.connect(self.host, self.userID, self.password, self.database)
            print "Able to connect to database"
        except:
            print 'Error initialising database'

    def __del__(self):
        self.db.close()


###########################3 enter student area ################################################

    def create_table_student_info(self):    
        #prepare the cursors
        cursor=self.db.cursor()
        #cursor.execute("SELECT VERSION()")
        #data=cursor.fetchone()
        sql='''CREATE TABLE  STUDENT_INFO(
                ID INT,
                NAME VARCHAR(100),
                MOBILE INT,
                EMAIL VARCHAR(100)
                PRIMARY KEY(ID) 
                )'''
        try:
            cursor.execute(sql)
            print "Created table STUDENT_INFO"
        except:
            print "Could not create table STUDENT_INFO. Table may already be existing"
        finally:
            cursor.close()

    def add_to_student_info(self,identity,name,mobile,email):
        cursor=self.db.cursor();
        sql="INSERT into DOC_FREQ values ("+identity+",'"+name+"',"+mobile+",'"+email"')"
        print sql #(debugging)
        try:
			cursor.execute(sql)
			print "Added data into student_info"    
			self.db.commit()
        except:
            print "Error adding idno:"+str(identity)+" name:"+(name)+" into Student_info"
        finally:
            cursor.close()

            ## update all details functions

######################################## exit student data area ##############################

#################################### enter finger print area ######################################3
    def create_table_fingerprint(self):    
        #prepare the cursors
        cursor=self.db.cursor()
        #cursor.execute("SELECT VERSION()")
        #data=cursor.fetchone()
        sql='''CREATE TABLE  FINGERPRINT(
                ID INT,
                FINGER_PRINT VARCHAR(200),
                PRIMARY KEY(ID) 
                )'''
        try:
            cursor.execute(sql)
            print "Created table fingerprint"
        except:
            print "Could not create table fingerprint. Table may already be existing"
        finally:
            cursor.close()
    ## enrol a student to it
    def add_to_fingerprint(self,identity,finger):
        cursor=self.db.cursor();
        sql="INSERT into FINGERPRINT values ("+identity+",'"+finger+"')"
        print sql #(debugging)
        try:
            cursor.execute(sql)
            print "Added data into fingerprint"    
            self.db.commit()
        except:
            print "Error adding idno:"+str(identity)+" template:"+(fingerprint)+" into fingerprint"
        finally:
            cursor.close()

    ## update a students finger print

    ## delete student 
#####################3 exit finger print tables with possible queries #############################


################## enter transaction table ########################################################

   def create_table_transactions_anc(self):    
        #prepare the cursors
        cursor=self.db.cursor()
        #cursor.execute("SELECT VERSION()")
        #data=cursor.fetchone()
        sql='''CREATE TABLE TRANSACTION_ANC(
                ID INT,
                AMOUNT_AT_ANC INT,
                TIME_STAMP INT,
                PRIMARY KEY(ID) 
                )'''
        try:
            cursor.execute(sql)
            print "Created table fingerprint"
        except:
            print "Could not create table fingerprint. Table may already be existing"
        finally:
            cursor.close()

    def add_to_transactions(self,identity,finger,time):
        cursor=self.db.cursor();
        sql="INSERT into FINGERPRINT values ("+identity+",'"+finger+"','"+time+"')"
        print sql #(debugging)
        try:
            cursor.execute(sql)
            print "Added data into fingerprint"    
            self.db.commit()
        except:
            print "Error adding idno:"+str(identity)+" template:"+(fingerprint)+" time"+(time)" into fingerprint"
        finally:
            cursor.close()
   
####################################### exit transaction table ################################

#################### enter server student transaction table ##########################33


## add transaction
## student table must also have left money in wallet(currently at 3K)
## student should be able to view his transactions (also shows spend patterns)
## daily earning of each shop for mining 

################### exit student server table ###########################

################# enter swd area ######################################

## should be able to push the transactions to swd
## should be able to add cash to wallet
## should be able to syn instantly the repleished amt to our server database

############## exit swd area #####################################

######### enter anc uncle area ####################

## daily monthly weekly analysis 
## daily earning which they have to collect from swd 

### exit anc uncle area ###################### 




