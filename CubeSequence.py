def multiple(n,sum):
    sum = 0
    for i in range(1,n):
        sum += i**3
    # print(sum)
    if sum%n==0:
        return True
    else:
        return False

num = int(input("Enter the number : "))
# sum = 0
# for i in range(1,num):
#     sum += i**3

# print(sum)

if multiple(num,sum)==True:
    print("Verified")
else:
    print("Not Verified")