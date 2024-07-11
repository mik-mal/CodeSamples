

n = 0
res = 0

for n in range(1,1000):
    if n%3 == 0:
        res = res + n
    elif n%5 == 0:
        res = res + n

print(n)
print(res)
