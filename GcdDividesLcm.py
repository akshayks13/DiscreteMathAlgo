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
        
    
def lcm(a,b):
    return (a//gcd(a,b))*b

def calculate_lcm(x, y):  
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


num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))

print(lcm(num1,num2))
print(gcd(num1,num2))

if lcm(num1,num2)%gcd(num1,num2)==0:
    print("It is divisible")
else:
    print("It is not divisible")
