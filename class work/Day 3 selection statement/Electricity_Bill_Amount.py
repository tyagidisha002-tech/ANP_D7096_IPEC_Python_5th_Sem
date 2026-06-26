'''---------------------Electricity Bill Discount ---------------------
 An electricity provider offers a 10% discount on the total bill amount if the customer's bill is ₹5,000 or more.
 Otherwise, no discount is applied. Write a Python program to accept the total bill amount from the user
 input the and display the final amount to be paid. 
  -------------------------------------------
  Sample Input 1 
  Enter the electricity bill amount: 6200 
  -------------------------------------------
  Sample Output 1 Discount Applied! 
  Final Bill Amount: ₹5580.0 
  --------------------------------------------
  Sample Input 2 
  Enter the electricity bill amount: 4200 
  --------------------------------------------
  Sample Output 2 
  No Discount Applied!
   Final Bill Amount: ₹4200 
   ---------------------------------------------------------------'''
   #-------------------Coding-------------------------------------------
   # Input the bill amount .
   bill_amount = float(input("Enter the bill amount"))
   #------------------Vaditing the bill amount---------------------------
   if(bill_amount<=0)
     exit("Enter the positive amount")
   #---------------------------------------------------------------------
   if(bill_amount>=5000): 
    discount = bill_amount*0.10
    total_amount =bill_amount-discount
    print("Discount Applied !")
    print("Final Bill Amount:",total_amount)
   else:
    print("No Discount Applied !")
  print("---------------------------------------------")