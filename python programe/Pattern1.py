n = int(input("Please Enter the total Number of Rows  : "))

 
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if((i+j)%2==1):          
            print('1', end = '  ')
        else:
            print('0', end = '  ')
        
    print()