def rprime(num,m):
    
    for num in range(num,m+1):
        
        if num > 1:
            for i in range(2, num):
                if(num % i)==0:
                    break
                
            else:
               print(num)
                    
x=int(input("enter 1st range:"))
y=int(input("enter 2nd range:"))
rprime(x,y)
