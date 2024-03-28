import equipments
import customer
import diet
import bill
def heading():
   print("\t","*"*80)
   print("\t\t\t\tSKY FITNESS TRAINING CENTRE")
   print("\t\t\t\tGET FIT NOW ")
   print("\t","*"*80)

 #Equipments menu
def equip():
  while True:
    heading()
    print("\t Equipments Information Menu")
    print("1. Add Equipments ")
    print("2. Modify Equipment")
    print("3. Delete Equipment")
    print("4. See Particular Equipment Detail")
    print("0. Exit")
    ans = int(input("Enter your choice :"))
    if ans==1:
       equipments.equip_add()
    elif ans==2:
        equipments.equip_Modify()
    elif ans==3:
        equipments.equip_Delete()
    elif ans==4:
        equipments.equip_search()
    else:
        break

#Customer Menu
def cust():
   while True:
       heading()
       print("\t CUSTOMER INFORMATION MENU")
       print("1.ADD DETAILS")
       print("2.MODIFY DETAILS")
       print("3.DELETE DETAILS")
       print("4.PARTICULAR CUSTOMER DETAILS")
       print("5.EXIT")
       ch=int(input("Enter your choice: "))
       if ch==1:
           customer.cust_add()
       elif ch==2:
           customer.cust_modify()
       elif ch==3:
           customer.cust_delete()
       elif ch==4:
           customer.cust_search()
       else:
            break

#Diet menu
def dietp():
   while True:
     heading()
     print("\t REPRORT ")
     print("1. Add Information ")
     print("2. Modify Information")
     print("3. Delete Information")
     print("4. see Particular report")
     print("0. Exit ")
     ans = int(input("Enter your choice :"))
     if ans==1:
        diet.dietp_add()
     elif ans==2:
        diet.dietp_modify()
     elif ans==3:
        diet.dietp_delete()
     elif ans==4:
        diet.dietp_search()
     else:
       break

#Bill Menu
def billing():
   while True:
      heading()
      print("\t BILLING INFORMATION")
      print("1. BILL GENERATE")
      print("2. PARTICULAR BILL")
      print("3. EXIT")
      ch=int(input("Enter your choice :"))
      if ch==1:
        bill.Billing_gent()
      elif ch==2:
        bill.One_bill()
      else:
        break

#Main menu
while True:
    heading()
    print("1. Equipments Information ")
    print("2. Customer Information")
    print("3. Bill Generation")
    print("4. Customer Report")
    print("0. Exit ")
    ans = int(input("Enter your choice :"))
    if ans==1:
       equip()
    elif ans==2:
        cust()
    elif ans==3:
        billing()
    elif ans==4:
        dietp()
    else:
        break
