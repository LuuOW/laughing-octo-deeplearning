import math

S = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]



def p(a):
    x=sum(a)/len(a)
    return x

def log2(a):
    a=math.log2(a)
    return a

def gini(a):
    h=2*p(a)*(1-p(a))
    return h

infogain=gini(S)-(len(A)/len(S))*gini(A)-(len(B)/len(S))*gini(B)
print(round(infogain,5))