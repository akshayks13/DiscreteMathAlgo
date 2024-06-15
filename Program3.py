# stmt = "For all x , P(x)."
# def P(x):
#     return x+1 > x

# forall = True 
# for x in [-2,-1,0,1,2]:
#     # Check if at least 1 is false
#     if P(x) == False:
#         forall = False

# print(stmt)
# print(forall)


stmt = "There exists an x, such that P(x)."
def P(x):
    return x**2 == 4

exists = False 
for x in [-2,-1,0,1,2]:
    # Check if at least 1 is false
    if P(x) == True:
        exists = True

print(stmt)
print(exists)