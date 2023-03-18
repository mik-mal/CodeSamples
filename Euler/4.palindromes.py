def reverse_num(n):
    
    n = str(n)
    length= len(n)
    n=n[length::-1]
    return int(n)


a = []

for n in range(100,1000):
    a.append(n)

b = a

c = []
for i in a:
    for j in b:
        c.append(i*j)
    
d = []

for k in c:
    if reverse_num(k) == k:
        d.append(k)
    
print(max(d))


