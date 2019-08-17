for row in range(16):
    for col in range(12):
        if(row not in {0,7}) and (col in {0}):
           print('* ',end='')
        if(col in {11}) and (row in {1,2,3,4,5,6}):
            print('* ',end='')
        if(row in {0,7}):
          print('* ',end='')
        
        elif(row==7):
          print('* ',end='')

        elif(row==8) and (col==0):
          print('* ',end='')
        
        elif(row==9) and (col==2):
          print('* ',end='')
        
        elif(row==10) and (col==4):
          print('* ',end='')
        
        elif(row==11) and (col==6):
          print('* ',end='')
        
        elif(row==12) and (col==8):
          print('* ',end='')
        
        elif(row==14) and (col==10):
          print('* ',end='')
        
        
        else:
            
            print('  ',end='')
    print('')