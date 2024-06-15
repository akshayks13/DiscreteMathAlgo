def gcd(a,b):
    if b>a:
        if a==0:
            return b
        else:
            return gcd(b%a,a)
    else:
        if b==0:
            return a
        else:
            return gcd(a%b,b)
        
def lcm(x, y):  
    # selecting the greater number  
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm    

def Factorial(n):
    if n==1:
        return 1
    else:
        return n*Factorial(n-1)
    
def Power(a,n):
    if n==0:
        return 1
    else:
        return a * Power(a,n-1)
    
def one(a,n):
    result = (Power(a,Factorial(n))-n)%gcd(a,n)
    return result

def two(a,b):
    if lcm(a,b)%gcd(a,b)==0:
        return True
    else:
        return False
    
def three():
    if Power(5,9)%31 == 6:
        return True
    else:
        return False
    
def four(n):
    sum = 0
    for i in range(1,n):
        sum += i**3
    # print(sum)
    if sum%n==0:
        return True
    else:
        return False

print("First Question") 
a = int(input("Enter the number for question 1 : "))
n = int(input("Enter the power for question 1 : "))
print(one(a,n))

print("Second Question") 
num1 = int(input("Enter the number 1 for question 2 : "))
num2 = int(input("Enter the number 2 for question 2 : "))
if two(num1,num2)==True:
    print("Its Verified")
else:
    print("Not Verified")

print("Third Question") 
print(three())

print("Fourth Question") 
num = int(input("Enter the number for question 4 : "))
if four(num)==True:
    print("Its Verified")
else:
    print("Not Verified")