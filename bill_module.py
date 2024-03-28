#Bill_Module
import mysql.connector as mc
from mysql.connector import errorcode

#Add Record
def Billing_gent():
  try:
    con=mc.connect(host="localhost",user="root",passwd="1234",database="fitness")
    cur=con.cursor()
    print("="*50)
    print("\t\tBill Generate")
    print("="*50)
    nm=input("\tEnter customer_name : ")
    mid=int(input("\tEnter membership ID : "))
    bno=int(input("\tEnter Bill no : "))
    bDt=input("\tEnter Bill Date : ")
    pm=input("\tEnter mode of payment : ")
    amt=eval(input("\tTotal Amount"))
    query="select name , amount from bill where MemberId={}".format(mid)
    cur.execute(query)
    data=cur.fetchall()
    if data !=[]:
       for row in data:
           name=row[0]
           amt=row[1]
           query="insert into bill values('{}',{},{},'{}','{}',{})".format(nm,mid,bno,bDt,pm,amt)
           cur.execute(query)
           con.commit()
           print("Record Inserted successfully")
           print("="*50)
    else:
        print("Not Found data")
        cur.close()
        con.close()

  except mc.Error as err:
    if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
        print("Wrong password or username")
    elif err.errno==errorcode.ER_BAD_DB_ERROR:
        print("Database not found")
    else:
        print(err)

#Display a bill at a time
def One_bill():
  try:
    con=mc.connect(host="localhost",user="root",passwd="1234",database="fitness")
    cur=con.cursor()
    name=input("\tEnter Customer Name : ")
    query="select * from bill where Name='{}'".format(name)
    cur.execute(query)
    data=cur.fetchall()
    if data!=[]:
       print("="*50)
       print("\t\t Bill Details ")
       print("="*50)
       for row in data:
             print("\tMembership ID: \t\t",row[1])
             print("\tBill Number:\t\t",row[2])
             print("\tBill Date: \t\t",row[3])
             print("\tMode of Payment: \t\t",row[4])
             print("\tTotal Amount: \t\t",row[5])
             print("="*50)
    else:
       print("\tData not exist")
       cur.close()
       con.close()

  except mc.Error as err:
    if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
       print("Wrong password or username")
    elif err.errno==errorcode.ER_BAD_DB_ERROR:
        print("Database not found")
    else  :
        print(err)