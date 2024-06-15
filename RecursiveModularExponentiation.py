def exponentMod(b,n,m):
    if n==0:
        return 1
    elif n%2 == 0:
        return (exponentMod(b,n/2,m)**2)%m
    else:
        return ((exponentMod(b,n//2,m)**2)%m * b%m)%m
    
base = int(input("Enter the number b : "))
power = int(input("Enter the power n : "))
modulas = int(input("Enter the number m : "))

print(exponentMod(base,power,modulas))