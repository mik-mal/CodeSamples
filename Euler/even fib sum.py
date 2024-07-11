
a = 1
b = 2
c = 3
fib = []

fib.append(b)

while c < 4000000:
    if c%2 == 0:
        fib.append(c)
    
    a=b
    b=c
    c = a+b

print(sum(fib))
