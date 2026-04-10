from sympy import nextprime, isprime, prevprime, factorint, primerange

def notsquarefree(a):
    for p, e in factorint(a).items():
        if e > 1:
            return True
    return False

def brute_force_check(n):
    p = 2
    while p < n:
        if notsquarefree(n-p) == True:
            return True
        else:
            p = nextprime(p)
    return False

def preload1():
    not_sq_frees = set([])
    for k in range(2,5*10**5):
        if notsquarefree(k) == True:
            not_sq_frees.add(k)
    return not_sq_frees

def preload2():
    not_sq_frees = []
    for k in range(2,10**4):
        if notsquarefree(k) == True:
            not_sq_frees.append(k)
    return not_sq_frees

def verify_ft(from_me, to_me, preload1, preload2):
    # preload1 should be a set of not-square-free integers <= 10**5
    # preload2 should be a list of not-square-free integers <= 10**4
    
    #populate a set of verified integers..
    verified = set()
    np = prevprime(from_me)
    while np < to_me:
        for s in preload1:
            if np + s not in verified:
                verified.add(np + s)
        np = nextprime(np + 10**4)

    #create a list of exceptional integers using brute force on integers not in verified..
    exceptions = []
    lpl2 = len(preload2)
    for m in range(from_me, to_me + 1):
        if m not in verified:
            found = False
            ind = 0
            while found == False:
                if isprime(m - preload2[ind]) == True:
                    found = True
                else:
                    if ind + 1 < lpl2:
                        ind += 1
                    else:
                        #print(m)
                        if brute_force_check(m) == False:
                            exceptions.append(m)
                        found = True # to ensure the proces terminates!
    return exceptions

# Run the code to locate all exceptions on 3 <= n <= 8*10**9. Only exceptions are: 3, 4, 5, 8, 24
pl1 = preload1()
pl2 = preload2()
print("Preloads generated.")

print(0, 1, verify_ft(3, 10**7, pl1, pl2))
for l in range(1,800):
    print(l, l+1, verify_ft(l*10**7, (l+1)*10**7, pl1, pl2))

"""
Output:

Preloads generated.

0 1 [3, 4, 5, 8, 24]
1 2 []
2 3 []
3 4 []
4 5 []
5 6 []
...
798 799 []
799 800 []
"""
