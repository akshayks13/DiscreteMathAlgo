
def conjn(p,q):
    return p and q

def disjn(p,q):
    return p or q

def impln(p,q):
    return not p or q

def Bi_condn(p,q):
    return (not p or q) and (p or not q)

def XOR(p,q):
    return (not p and q) or (p and not q)

def negation(p):
    return not p


print("         Conjunction         ")
print("-------------------------------------------------")
print("|        p       |       q       |       r       |")
print("-------------------------------------------------")
for p in [True , False]:
    for q in [True , False]:
        a=conjn(p,q)
        print('|','\t',p,'\t','|','\t',q,'\t','|','\t',a,'\t','|')
        print("--------------------------------------------------")


print("         Disjunction         ")
print("-------------------------------------------------")
print("|        p       |       q       |       r       |")
print("-------------------------------------------------")
for p in [True , False]:
    for q in [True , False]:
        a=disjn(p,q)
        print('|','\t',p,'\t','|','\t',q,'\t','|','\t',a,'\t','|')
        print("--------------------------------------------------")


print("         Implication         ")
print("-------------------------------------------------")
print("|        p       |       q       |       r       |")
print("-------------------------------------------------")
for p in [True , False]:
    for q in [True , False]:
        a=impln(p,q)
        print('|','\t',p,'\t','|','\t',q,'\t','|','\t',a,'\t','|')
        print("--------------------------------------------------")



print("         Bi-Conditinal         ")
print("-------------------------------------------------")
print("|        p       |       q       |       r       |")
print("-------------------------------------------------")
for p in [True , False]:
    for q in [True , False]:
        a=Bi_condn(p,q)
        print('|','\t',p,'\t','|','\t',q,'\t','|','\t',a,'\t','|')
        print("--------------------------------------------------")



print("         XOR         ")
print("-------------------------------------------------")
print("|        p       |       q       |       r       |")
print("-------------------------------------------------")
for p in [True , False]:
    for q in [True , False]:
        a=XOR(p,q)
        print('|','\t',p,'\t','|','\t',q,'\t','|','\t',a,'\t','|')
        print("--------------------------------------------------")