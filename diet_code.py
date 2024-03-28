#Diet Module
import mysql.connector as mc
from mysql.connector import errorcode

# Add Record
def dietp_add():
  try:
    con=mc.connect(host="localhost",user="root",passwd="kriti02",database="fitness")
    cur=con.cursor()
    print("="*50)
    print("\t\tAdd Record")
    print("="*50)
    mid=int(input("\tEnter Customer's Membership ID:"))
    name=input("\tEnter Name of Customer:")
    height=eval(input("\tEnter height in Metres:"))
    weight=eval(input("\tEnter Weight in KG:"))
    bmi=(weight)/(height**2)
    wt=int(input("\tEnter Workout Time:"))
    diet=input("\tEnter Diet Type:")
    sql="insert into diet values({},'{}',{},{},{},{},'{}')".format(mid,name,height,weight,bmi,wt,diet)
    cur.execute(sql)
    con.commit()
    print("Record Inserted...............")
    print("="*50)
    cur.close()
    con.close()
  except mc.Error as err:
    if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
       print("wrong password or user name")
    elif err.errno==errorcode.ER_BAD_DB_ERROR:
       print("database not exist")
    else:
       print(err)

# Search Records
def dietp_search():
  try:
    con=mc.connect(host="localhost",user="root",passwd="1234",database="fitness")
    cur=con.cursor()
    mid=int(input("Enter Membership ID :"))
    sql="select * from diet where MemberId={}".format(mid)
    cur.execute(sql)
    data=cur.fetchall()
    if data!=[]:
       for row in data:
           print("\tCustomer Name:",row[1])
           print("\tHeight:",row[2])
           print("\tWeight:",row[3])
           print("\tBMI:",row[4])
           print("\tWorkout Time:",row[5])
           print("\tDiet Type:",row[6])
           return mid

    else:
        print("\tRecord not exist")
        return -1
        cur.close()
        con.close()

  except mc.Error as err:
    if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
       print("wrong password or user name")
    elif err.errno==errorcode.ER_BAD_DB_ERROR:
       print("database not exist")
    else:
        print(err)

# Modification
def dietp_modify():
   try:
     con=mc.connect(host="localhost",user="root",passwd="1234",database="fitness")
     cur=con.cursor()
     print("="*50)
     print("\t\tModify Record")
     print("="*50)
     mid=dietp_search()
     if mid!=-1:

        ch=input("\tModify it (y/n)")
        if ch=='y':
           name=input("\tEnter Name of Customer:")
           height=eval(input("\tEnter height in Metres:"))
           weight=eval(input("\tEnter Weight in KG:"))
           bmi=(weight)/(height**2)
           wt=int(input("\tEnter Workout Time:"))
           diet=input("\tEnter Diet Type:")
           sql="update diet set name='{}',height_metres={},weight_kg={},BMI={},Workout_Time={},Diet_Type='{}'".format(name,height,weight,bmi,wt,diet)
           cur.execute(sql)
           con.commit()
           print("Record Updated...............")
           print("="*50)
           cur.close()
           con.close()

   except mc.Error as err:
      if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
         print("wrong password or user name")
      elif err.errno==errorcode.ER_BAD_DB_ERROR:
         print("database not exist")
      else:
         print(err)

# Delete
def dietp_delete():
  try:
    con=mc.connect(host="localhost",user="root",passwd="1234",database="fitness")
    cur=con.cursor()
    print("="*50)
    print("\t\tDelete Record")
    print("="*50)
    mid=dietp_search()
    if mid!=-1:
       ch=input("\tDelete it (y/n)")
    if ch=='y':
       sql="delete from diet where MemberId='{}'".format(mid)
       cur.execute(sql)
       con.commit()
       print("Record Deleted...............")
       print("="*40)
       cur.close()
       con.close()
  except mc.Error as err:
    if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
        print("wrong password or user name")
    elif err.errno==errorcode.ER_BAD_DB_ERROR:
        print("database not exist")
    else:
       print(err)