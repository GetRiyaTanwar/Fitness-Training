#equipment module
import mysql.connector as mc
from mysql.connector import errorcode

#Add Record
def equip_add():
  try:
    con=mc.connect(host="localhost",user="root",passwd="1234",database="fitness")
    cur=con.cursor()
    print("="*50)
    print("\t\tAdd Record")
    print("="*50)
    mid=input("\tEnter Machine ID:")
    mname=input("\tEnter Machine name:")
    bname=input("\tEnter Brand Name:")
    Type=input("\tEnter Machine Type:")
    num=int(input("\tEnter number of machines available:"))
    sql="insert into equipments values({},'{}','{}','{}',{})".format(mid,mname,bname,Type,num)
    cur.execute(sql)
    con.commit()
    print("Record Inserted")
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

# Search Record
def equip_search():
  try:
    con=mc.connect(host="localhost",user="root",passwd="1234",database="fitness")
    cur=con.cursor()
    mid=input("Enter Machine ID:")
    sql="select * from equipments where MachineId={}".format(mid)
    cur.execute(sql)
    data=cur.fetchall()
    if data!=[]:
       for row in data:
            print("\tMachine name:",row[1])
            print("\tBrand Name:",row[2])
            print("\tMachine Type:",row[3])
            print("\tNumber of Machines:",row[4])
            return mid
    else:
        print("\tRecordnot exist")
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

 # Modify record
def equip_Modify():
   try:
       con=mc.connect(host="localhost",user="root",passwd="1234",database="fitness")
       cur=con.cursor()
       print("="*50)
       print("\t\tModify Record")
       print("="*50)
       mid=equip_search()
       if mid!=-1:
            ch=input("\tModify it (y/n)")
            if ch=='y':
                name=input("\t\tEnter Machine Name:")
                bname=input("\t\tEnter Brand Name:")
                Type=input("\t\tEnter Machine Type:")
                num=int(input("\t\tEnter number of machines:"))
                sql="update equipments set MachineName='{}',brand='{}',Type='{}',number={}".format(name,bname,Type,num)
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

# Delete Record
def equip_Delete():
    try:
       con=mc.connect(host="localhost",user="root",passwd="1234",database="fitness")
       cur=con.cursor()
       print("="*50)
       print("\t\tDelete Record")
       print("="*50)
       mid=equip_search()
       if mid!=-1:

        ch=input("\tDelete it (y/n)")
        if ch=='y':
           sql="delete from equipments where MachineId='{}'".format(mid)
           cur.execute(sql)
           con.commit()
           print("Record Deleted...............")
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
