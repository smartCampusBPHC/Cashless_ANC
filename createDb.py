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
   







