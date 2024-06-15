def Fibonacci(n):
    # Check if n is 0
    # then it will return 0
    if n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 

print("Enter a postive number to calculate the Fibonacci series ")
num=-1
while(num<0):
    num = int(input("Enter the no. of terms : "))
    for i in range(num):
        print(Fibonacci(i))
