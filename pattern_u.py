for row in range(7):
    for col in range(5):
        if(col in {0,4}) and (row not in {0}):
            print('* ',end='')
        elif(col in {0,1,2,3}) and (row not in {0,1,2,3,4,5}):

            print('* ',end='')
        

        else:
            print('  ',end='')
    print('')