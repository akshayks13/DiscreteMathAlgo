
def q1(p,q,r):
    return (not p or q) or (not q or r)

def q2(p,q,r):
    return (not p or q) and (not q or r)

def q3(p,q,r):
    return (not((not p or q) and (not q or r)) or (not p or q))

def q4(p,q,r):
    return(not((p or q)and(not p or r)) or (q or r))

def q5(p,q,r):
    return(not((p or q) and (not p or q) and (not q or r)) or r)

def tauto(q1):
    return

print("          q1          ")
print("------------------------------------------------------------------")
print("|        p       |       q       |       r       |       a       |")
print("------------------------------------------------------------------")
for p in [True , False]:
    for q in [True , False]:
        for r in [True,False]:
            a=q1(p,q,r)
            print('|','\t',p,'\t','|','\t',q,'\t','|','\t',r,'\t','|','\t',a,'\t','|')
            print("------------------------------------------------------------------")

s=True
for p in [True , False]:
    for q in [True , False]:
        for r in [True,False]:
            a=q1(p,q,r)
            s= s and a
if s == True:
        print('q1 is a Tautology')
else:
    print("q2 is not a Tautology")




print("          q2          ")
print("------------------------------------------------------------------")
print("|        p       |       q       |       r       |       a       |")
print("------------------------------------------------------------------")
for p in [True , False]:
    for q in [True , False]:
        for r in [True,False]:
            a=q2(p,q,r)
            print('|','\t',p,'\t','|','\t',q,'\t','|','\t',r,'\t','|','\t',a,'\t','|')
            print("------------------------------------------------------------------")

s2=True
for p in [True , False]:
    for q in [True , False]:
        for r in [True,False]:
            a=q2(p,q,r)
            s2= s2 and a

if s2 == True:
        print('q2 is a Tautology')
else:
    print("q2 is not a Tautology")


print("          q3          ")
print("------------------------------------------------------------------")
print("|        p       |       q       |       r       |       a       |")
print("------------------------------------------------------------------")
for p in [True , False]:
    for q in [True , False]:
        for r in [True,False]:
            a=q3(p,q,r)
            print('|','\t',p,'\t','|','\t',q,'\t','|','\t',r,'\t','|','\t',a,'\t','|')
            print("------------------------------------------------------------------")


s3=True
for p in [True , False]:
    for q in [True , False]:
        for r in [True,False]:
            a=q3(p,q,r)
            s3= s3 and a

if s3 == True:
        print('q3 is a Tautology')
else:
    print("q3 is not a Tautology")



print("          q4          ")
print("------------------------------------------------------------------")
print("|        p       |       q       |       r       |       a       |")
print("------------------------------------------------------------------")
for p in [True , False]:
    for q in [True , False]:
        for r in [True,False]:
            a=q4(p,q,r)
            print('|','\t',p,'\t','|','\t',q,'\t','|','\t',r,'\t','|','\t',a,'\t','|')
            print("------------------------------------------------------------------")

s4=True
for p in [True , False]:
    for q in [True , False]:
        for r in [True,False]:
            a=q4(p,q,r)
            s4= s4 and a

if s4 == True:
        print('q4 is a Tautology')
else:
    print("q2 is not a Tautology")



print("          q5          ")
print("------------------------------------------------------------------")
print("|        p       |       q       |       r       |       a       |")
print("------------------------------------------------------------------")
for p in [True , False]:
    for q in [True , False]:
        for r in [True,False]:
            a=q5(p,q,r)
            print('|','\t',p,'\t','|','\t',q,'\t','|','\t',r,'\t','|','\t',a,'\t','|')
            print("------------------------------------------------------------------")

s5=True
for p in [True , False]:
    for q in [True , False]:
        for r in [True,False]:
            a=q5(p,q,r)
            s5= s5 and a

if s5 == True:
        print('q5 is a Tautology')
else:
    print("q5 is not a Tautology")
