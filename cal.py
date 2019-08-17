 
while True:
    print("1.add   2. sub   3.mul  4.div")
    a=int(input("Enter The Choice  : "))
    d=a
    ans=0
    num1=int(input("Enter the number :: "))
    num2=int(input("Enter the number :: "))
    if d==1:
        ans=num1+num2
        print("ans =",ans)
    elif d==2:
        ans=num1-num2
        print("ans =",ans)
    elif d==3:
        ans=num1*num2
        print("ans =",ans)
    elif d==4:
        ans=num1/num2
        print("ans =",ans)  
    else:
        print("WRONG CHOICE::")
