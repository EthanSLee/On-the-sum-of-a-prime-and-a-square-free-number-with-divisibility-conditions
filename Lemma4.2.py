# The following code deals with odd n only, even n are verified using the is_good function under Lemma4.3.py.

from sympy import prevprime, primerange, nextprime, factorint, isprime

def coprime_weaker(a,b):
    fi_A = factorint(a)
    fi_B = factorint(b)
    for p in fi_A:
        if p in fi_B.keys() and p > 2:
            return False
    return True

def nextcoprimesquarefree_evens(y,coprime_to):
    i = 2
    while i > 0:
        fi = factorint(y + i)
        condition_met = [coprime_weaker(j,y+i) for j in coprime_to] 
        if max(fi.values()) == 1 and False not in condition_met:
            return y + i
        i += 2

def is_good(n,v):
    sf = 2 #the first nontrivial squarefree
    cpt = []
    while sf < n:
        if isprime(n-sf) == True:
            cpt.append(sf)
        if len(cpt) < v+1:
            sf = nextcoprimesquarefree_evens(sf, cpt)
        else:
            return True, cpt
    return False, cpt

def is_prime_times_power_of_two(n):
    while n % 2 == 0:
        n = n/2
    return isprime(n)

def issquarefree(y):
    fi = factorint(y)
    if max(fi.values()) == 1:
        return True
    else:
        return False

def is_sqarefree_times_power_of_two(n):
    while n % 2 == 0:
        n = n/2
    return issquarefree(n)

def verify_ft_semiprimes_small(from_me, to_me, N=3):
    not_verified = []
    m = from_me
    while m <= to_me+1:
        ig = is_good(m,N)
        if ig[0] == False:
            #print(m)
            not_verified.append(m)
        m += 2
    return not_verified

def verify_ft_semiprimes_quick(from_me, to_me):
    small_primes = set()
    p = 2
    while p < 500:
        small_primes.add(p)
        p = nextprime(p)

    """
    pc_primes = set()
    p = prevprime(from_me - 3*10**3)
    while p < to_me:
        pc_primes.add(p)
        p = nextprime(p+10**4)
    """
    
    num_representations = {}
    q = prevprime(from_me - 10**3)
    while q < to_me:
        for p1 in small_primes:
            for p2 in small_primes:
                if p1 == p2:
                    m = q + 2*p1
                    if m not in num_representations:
                        num_representations[m] = 1
                    else:
                        num_representations[m] += 1
                else:
                    m = q + p1 + p2
                    for a1, a2 in [(p1,p1), (q,p1), (q,p2)]:
                        #print(a1,a2,[(p1,p1), (q,p1), (q,p2)])
                        if is_prime_times_power_of_two(a1 + a2) == True:
                            if m not in num_representations:
                                num_representations[m] = 1
                            else:
                                num_representations[m] += 1
        #print(q, len(num_representations))
        q = nextprime(q + 10**3)
    #print("Generated!")
    
    not_verified = []
    m = from_me
    while m <= to_me:
        if m not in num_representations or num_representations[m] < 2:
            #print(m)
            reps = []
            q = 3
            while 2*q < m and len(reps) < 2:
                if is_prime_times_power_of_two(m-q) == True:
                    #print(q,m-q)
                    reps.append((q,m-q))
                q = nextprime(q)
            #print(m, reps)
            if len(reps) < 2:
                not_verified.append(m)
        #else:
        #    print(m)
        m += 2
    return not_verified


exptons = verify_ft_semiprimes_small(5, 10**5, 2)
for e in exptons:
    print(e)
print("\n")

exptons = verify_ft_semiprimes_small(5, 10**5, 3)
for e in exptons:
    print(e)

"""
Output:

5
7
9
11
15
23
35


5
7
9
11
13
15
17
19
21
23
27
31
35
47
59
"""
