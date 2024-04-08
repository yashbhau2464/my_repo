# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:25:43 2024

@author: ACER
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
num=int(input("enter a number:'"))
if num >0:
     print(num)


num= int (input("enter a number"))
if num>0:
    print(num)
    
    
    #else in an if statement
    num +int(int(input('enter yet another number:')))
    if num<0:
        print('Its negative')
    else:
        print('its not negative')
        
        
        
        #the use of else
savings =float(input("enter how much you have in savings:")) 
if savings ==  0: 
    print("sorry no savings") 
elif savings<500:
    print('well done')
elif savings<1000:
    print('thats the tidy sum')
elif savings>1000:
    print('you are a millionare')
else:
    print('thank you')
    
 
    #Q1-Mailing address
 
    print("some address line 1") 
    print("some address line 2")   
    print("City")
    print("State and postal code")
    print("country")
    print("Telephone no:123456789") 

 
    #Q2-Area of room
length = float(input("Enter the length of the room in feet:"))
width = float(input("Enter the width of the room in feet:"))  
area = length *width
print("the Area of the room is",area,"squarefeet")
    
 
    #Q3-
length = float(input("Enter the length of the field in feet:"))
width = float(input("Enter the width of the field in feet:"))  
area=length*width/43560
print("area of field is",area,"acre")
    
 #########################################################################
#Q4-
#Bottle deposits

small = int(input("Enter the number of small containers: "))
large = int(input("Enter the number of large containers: "))
deposit1 = 0.10
deposit2 = 0.25
refund = (small * deposit1) + (large * deposit2)
refund_text="Total refund: ${:.2f}"
print(refund_text.format(refund))

#########################################################################
#Q5-
#Tax and Tip

meal_cost=float(input("Enter cost of the meal: "))
tax=0.20*meal_cost
tip=0.18*meal_cost
print("Meal cost= ${:.2f}".format(meal_cost))
print("Tax= ${:.2f}".format(tax))
print("Tip= ${:.2f}".format(tip))
print("Total= ${:.2f}".format(meal_cost+tax+tip))

#########################################################################
#Q6-
#Height Units

print("Enter height")
feet=int(input("Enter number of feet: "))
inches=int(input("Enter inches: "))
height=(12*feet+inches)*2.54
print(f"Your height in centimeters is {height} cms")
 
    
 
    
 
    
 
    
 
================================================================    
    
###################################################################
    '''Day4'''
    
   # for loop
        
start,end=4,19
for num in range(start,end+1):
   if num % 2!=0:
      print(num,end="")
      
      
      
start,end=4,19
for num in range (start,end+1):
    if num%2==0:
       print(num,end="")
---------------------------------------------
 #global variable 
----------------------------------------------
    
x="awesome"
def my_function():
    print("python is "+x)
my_function()
      
      
      
x="awesome"
def my_function():
x="fantastic" 
   print("python is "+x)         
my_function()
      -------------------------
             #dictionary
      -------------------------
      
x={"name":"Yash","age":20}
print(type(x))      
      
      
x=1
y=2.3
z=2+3j
print(type(x))
print(type(y))
print(type(z))



#string slicing
x=this is python




x="hello world"
print(x.split(" "))
      
      
      
x="this is python and it is powerful"
print(x.find("and"))
      
##################################################
x="Hello"
y="World"
print(x+y)
print(x+" "+y)

#####################################################
x=19
y="my name is Yash"
print(x+y)





##################################################################


print(my name is yash and my age is{x})
quantity=3
item_no=54
price=67
print(f"I want {quantity}pieces and item number is {item_no) and price is {price}")
      
###################################################################      
##format method      

  print "my name is yash and my age is{x}"
  quantity=3
  item_no=54
  price=67
  print("I want {0}pieces and item number is {1} and price is {100}")
      print(my_order.format(quantity,item_number,price))
      
#########################################################
#escape characters

print("Myname is""\yash")  


-
##########################################
#print
print(3**(3-2)/3*4+6)


##########################################

           '''LIST'''
#datastructure,derived type 

#################################################


-------------------------------------------
lst=["cherry","banana","apple"]
print(lst)

----------------------------------------------

lst=["cherry","banana","apple"]
print(lst[0])
print(lst[2])
---------------------------------------------------
#################################################


'''APPEND()'''#add element at the end if the list

#################################################
lst=["cherry","banana","apple"]
lst.append("mango")
print(lst)

---------------------------------------------------------------
lst=["cherry","banana","apple"]
lst.clear()
print(lst)

--------------------------------------------------------------
 
lst=["cherry","cherry","apple"]
lst.count("cherry")

----------------------------------------------

lst=["cherry","banana","apple"]
lst.extend("mango")
print(lst)

-------------------------------------------------
lst1=[0,1,2,3,]
lst=[4,5,6]
lst.extend(lst1)
print(lst)

-----------------------------------------------
#pop()
--------------------------------------------
lst=["cherry","banana","apple"]  
lst.pop(2)
print(lst)
---------------------------------------------

------------------------------------------------
lst=["cherry","cherry","apple"]
lst.remove("cherry")
print(lst)
----------------------------------------------
lst=["cherry","cherry","apple"]
lst.reverse()
print(lst)
--------------------------------------------------
lst=["cherry","banana","apple"] 
lst.sort()
print(lst)
-----------------------------------------------
##################################################     
      '''TUPPLE'''
      #properties
      #immutable
      #allowes mixed values
      #multiple datatype
      
      
      
##################################################

tup=("cherry","banana","apple")
print (tup)
print(tup[2])
 ----------------------------------------------
#once the tupple is created we cannot change its value

x=("cherry","banana","apple")
x[1]='kiwi'
----------------------------------
#convernt list to tupple
x=tuple(y)
print(x)
---------------------------------------
tuple1=("a","b","c")
tuple2=(1,2,3)
tup1=tuple1+tuple2
print(tup1)

###################################################
    '''DICTIONARY'''
    
    #key and value pair
###############################################
dict1={"brand":"maruti","model":"234565","year":2024}
print(dict1)
print(len(dict1))
    
---------------------------------------------
dict1={"brand":["maruti","mahindra","lamborgini"],"model":['2','3','4','5','6'],"year":[2004,2003,2004,2005]}
print(dict1)
print(len(dict1))

-------------------------------------------------------------
dict1.get("model")
dict1.keys()
-------------------------------------------------------


==============================================
####################################################
          '''DAY-5'''
#################################################
#add

car={"brand":"maruti","model":"234565","year":2024}
x=car.keys()
print(x)
car["color"]="white"
car
x=car.keys()
print(x)
------------------------------------------------
#remove

car={"brand":"maruti","model":"234565","year":2024}
car.pop("model")
print(car)
















    
