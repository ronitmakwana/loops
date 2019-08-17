col=input("enter no:")
print(col)
row=input("enter no:")
print(row)

if(col in {0,4}) and (row not in {0}):
    print('* ',end='')

elif(col in {0,1,2,3}) and (row not in {0,1,2,3,4,5}):
    print('* ',end='')
        
else:
     print('  ',end='')
     
     print('')