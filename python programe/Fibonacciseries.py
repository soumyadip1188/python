def rec_fibo(x):
    if x<=1:
        return x
    else:
        return(rec_fibo(x-1) +rec_fibo(x-2))

n=int(input("How many terms?"))

if n<=0:
    print("enter a positive integer: ")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(rec_fibo(i))