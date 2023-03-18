from cmath import sqrt
from genericpath import exists


lista = []

for i in range(1,1000):
    lista.append(float(i))

listb = lista
result = []

for a in lista:
    for b in listb:
        c = abs(sqrt(a*a + b*b))
        if a + b + c == 1000:
            result = [a, b, c]
            break
    if len(result) > 0:
        break

y=1
for x in result:
    y = y*x

print(y)