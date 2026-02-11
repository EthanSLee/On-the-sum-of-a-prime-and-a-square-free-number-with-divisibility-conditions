from sympy import nextprime, isprime, prevprime, factorint, primerange

def squarefree_odds(a):
    for p, e in factorint(a).items():
        if p > 2 and e > 1:
            return False
    return True

def coprime(a,b):
    fa = factorint(a)
    fb = factorint(b)
    for p in fa:
        if p in fb:
            return False
    return True

def coprime_weaker(a,b):
    fa = factorint(a)
    fb = factorint(b)
    for p in fa:
        if p in fb and p > 2:
            return False
    return True

def three_progressions():
    options = set()
    p = 3
    while p < 5000:
        q = nextprime(p)
        while q < p + 500:
            if squarefree_odds(p+q) == True and False not in [coprime_weaker(p+q,j[-1]) for j in options]:
                options.add((p,q,p+q))
            q = nextprime(q)
        p = nextprime(p)
    return options

def remove_excess_powers_of_two(m):
    while m % 2 == 0:
        m = m/2
    return m

def squarefree(a):
    for p, e in factorint(a).items():
        if e > 1:
            return False
    return True

def check(w):
    reps exp_ionc= []
    pr = 2
    while pr < w:
        if squarefree(w - pr) == True and False not in [coprime_weaker(w - pr,j) for j in reps]:
            reps.append(w-pr)
            if len(reps) == 3:
                return True
        pr = nextprime(pr)
    return False

def proc(fromme, upto, preloads):
    representations = {}
    prime = prevprime(fromme - 1000)
    while prime < upto:
        for a,b,c in preloads:
            e = 0
            m = prime + c*(2**e)
            while m < upto:
                if m not in representations:
                    representations[m] = 1
                else:
                    representations[m] += 1
                e += 1
                m = prime + c*(2**e)
        prime = nextprime(prime + 500) # Toggle 500 to increase/decrease speed (500 good for width of 10**6..)

    exceptions = []
    w = fromme
    while w <= upto:
        if w not in representations or representations[w] < 3:
            if check(w) == False:
                exceptions.append(w)
        w += 2
    return exceptions

tp = three_progressions()
print("Prime tuples generated.") 

ell = 1
print(ell, proc(10**5 + 1, ell*10**6,tp))
ell += 1
while ell*10**6 <= 4.81*(10**9):
    print(ell, proc((ell - 1)*(10**6) + 1, ell*(10**6),tp))
    ell += 1

"""
Output:

Prime tuples generated.

1 []
2 []
3 []
4 []
5 []
6 []
7 []
8 []
...
4807 []
4808 []
4809 []
4810 []
"""
