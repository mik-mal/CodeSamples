
a = []

for i in range(1,101):
    a.append(i)

b = []

for j in a:
    b.append(j**2)

print(abs(sum(b)-sum(a)**2))