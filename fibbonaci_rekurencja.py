def fibbonaci_rekurencja(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbonaci_rekurencja(n-2)+fibbonaci_rekurencja(n-1)
n=int(input('Podaj liczbę: '))
print(fibbonaci_rekurencja(n))