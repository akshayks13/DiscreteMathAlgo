def Power(a,n):
    if n==0:
        return 1
    else:
        return a * Power(a,n-1)
    
num = int(input("Enter the number : "))
pow = int(input("Enter the power : "))
print(Power(num,pow))