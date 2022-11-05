def zmien(n,systemik):
    r=1
    zamienione=[]
    while r!=0:
        r=n//systemik
        c = x(n%systemik)
        zamienione.append(c)
        n=r
        wynik=zamienione[::-1]
    return wynik
def x(n):
    if n<=9:
        return n
    else:
        return chr(55+n)
n=int(input("Podaj liczbę: "))
systemik=int(input('Podaj system: '))
print(zmien(n,systemik))
