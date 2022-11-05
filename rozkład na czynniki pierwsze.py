def rozklad(n):
    i=2
    while n>1 and i*i<=n:
        while n%i==0:
            print(i)
            n=n/i
        i+=1
    if n>1:
        print(n)
n=int(input("Podaj liczbę, którą chcesz rozłożyć: "))
rozklad(n)