def factorial(n):
    fact = 1
    while(n!=0):
        fact=fact*n
        n=n-1
    return fact
def Krishnamurty(n):
    s = 0
    temp = n
    while(temp!=0):
        rem=temp%10
        s=s+factorial(rem)
        temp=temp//10
    return(s==n)
    
n=int(input("enter a numberto check if it's a Krishnamurty number or not:"))
if(Krishnamurty(n)):
    print("Krishnamurty Number.")
else:
    print("Not a Krishnamurty Number.")