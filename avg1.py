
from array import array as var
class Student:

    d=int(input("Enter The Numbers:"))
    
    
    a=d
    c=0
    var=[]
    sum =0
  #  for i in range(c , d):
    i=1
    while i<=d:
     num=str(input("Enter The Student Name : "))
     print(i,".",num)
     i=i+1
    
       
    
        
 #   while c<a:
            
           # num=str(input("Enter The Student Name : "))
     num=int(input("Enter The Student Marks in Maths : "))
     num=int(input("Enter The Student Marks in English : "))
     num=int(input("Enter The Student Marks in Physics : "))
        
        
            
     sum=sum+num
     var.append(num)
     c=c+1

     print("The total +",sum)      
     print(len(var))
     c=len(var)
     ave=sum/c
     print("Average =",ave)

print("Operation is successfull")
            


        
