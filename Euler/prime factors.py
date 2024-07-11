def primes_method5(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

a = 600851475143
b = int(a**0.5)+1
c = primes_method5(b)
c.reverse()
d = []

for n in c:
    if a % n == 0:
        d.append(n)
        break

print(d)
