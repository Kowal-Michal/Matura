def fib_iteracja(n):
    a=0
    b=1
    for i in range (0,n):
        print(b)
        b+=a
        a=b-a
n=int(input('Podaj liczbę: '))
print(fib_iteracja(n))


