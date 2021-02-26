def counting(number):
    count=0
    while(number > 0):
        r=number%10
        
        if(r!=0):
            count=count+1
            
        number=number // 10
    return count
    
number=int(input("please enter any number:"))
count=counting(number)
print("\n Number of digits in a given number =%d" %count)