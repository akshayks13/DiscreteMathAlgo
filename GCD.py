def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
    
num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))

if num1>num2:
    print(gcd(num2,num1))
else:
    print(gcd(num1,num2))