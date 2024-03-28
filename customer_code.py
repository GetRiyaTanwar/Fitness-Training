# Customer Module
import mysql.connector as mc
from mysql.connector import errorcode

#Add Record
def cust_add():
   try:
      con=mc.connect(host="localhost",user="root",passwd="1234",database="fitness")
      cur=con.cursor()
      print("="*50)
      print("\t\tAdd Record")
      print("="*50)
      mid=int(input("\tEnter Membership ID : "))
      nm=input("\tEnter Name of Customer : ")
      ph=int(input("\tEnter phone Number : "))
      doj=input("\tEnter Date of joining : ")
      age=int(input("\tEnter Age of customer: "))
      gen=input("\tEnter Gender of customer : ")
      tn=input("\tEnter Name of Trainer : ")
      query="insert into customer values({},'{}',{},'{}',{},'{}','{}')".format(mid,nm,ph,doj,age,gen,tn)
      cur.execute(query)
      con.commit()
      print("Record Inserted successfully...")
      print("="*50)
      cur.close()
      con.close()
   except mc.Error as err:
       if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
           print("Wrong password or username")
       elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
       else:
            print(err)

#Search Records
def cust_search():
  try:
    con=mc.connect(host="localhost",user="root",passwd="1234",database="fitness")
    cur=con.cursor()
    mid=input("Enter Membership ID : ")
    query="select * from customer where MemberId={}".format(mid)
    cur.execute(query)
    data=cur.fetchall()
    if data!=[]:
       for row in data:
           print("\tCustomer Name:",row[1])
           print("\tPhone number:",row[2])
           print("\tDate of joining:",row[3])
           print("\tCustomer Age:",row[4])
           print("\tCustomer Gender:",row[5])
           print("\tTrainer Name:",row[6])
           return mid
    else:
       print("\tRecord not found")
       return -1
       cur.close()
       con.close()
  except mc.Error as err:
    if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
        print("Wrong password or username")
    elif err.errno==errorcode.ER_BAD_DB_ERROR:
        print("Database not found")
    else:
        print(err)

#Customer Modification
def cust_modify():
  try:
   con=mc.connect(host="localhost",user="root",passwd="1234",database="fitness")
   cur=con.cursor()
   print("="*50)
   print("\t\tModify Record")
   print("="*50)
   mid=cust_search()
   if mid!=-1:
    ch=input('\tModify it (y/n)')
   if ch=='y':
    nm=input("\tEnter Name of Customer : ")
    ph=input("\tEnter phone Number : ")
    doj=input("\tEnter Date of joining : ")
    age=int(input("\tEnter Age of customer: "))
    gen=input("\tEnter Gender of customer : ")
    tn=input("\tEnter Name of Trainer : ")
    query="update customer set name='{}',phno='{}',doj='{}',age={},gender='{}',trainer_name='{}'".format(nm,ph,doj,age,gen,tn)
    cur.execute(query)
    con.commit()
    print("Record Modified successfully...")
    print("="*50)
    cur.close()
    con.close()
  except mc.Error as err:
    if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
       print("Wrong password or username")
    elif err.errno==errorcode.ER_BAD_DB_ERROR:
       print("Database not found")
    else:
       print(err)

#Customer Delete
def cust_delete():
  try:
   con=mc.connect(host="localhost",user="root",passwd="1234",database="fitness")
   cur=con.cursor()
   print('='*50)
   print("\t\tDelete Record")
   print('='*50)
   mid=cust_search()
   if mid!=-1:
    ch=input("\tDelete this(y/n)")
   if ch=='y':
    query="delete from customer where MemberId={}".format(mid)
    cur.execute(query)
    con.commit()
    print("Record Deleted sucessfully...")
    print("="*50)   
    cur.close()
    con.close()
  except mc.Error as err:
    if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
      print("Wrong password or username")
    elif err.errno==errorcode.ER_BAD_DB_ERROR:
      print("Database not found")
    else:
      print(err)