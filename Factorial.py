
def Factorial(n):
    if n==1:
        return 1
    else:
        return n*Factorial(n-1)
    
num = int(input("Enter a number : "))
print(Factorial(num))