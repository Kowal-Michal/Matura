# sprawdza czy n jest liczbą doskonałą
def liczba_doskonala(n):
    dzielniki = []
    suma = sum(dzielniki[1:])
    for i in range (1,n-1):
        if n%i==0:
            dzielniki.append(i)
        else:
            continue
    if n==sum(dzielniki[0:]):
        return True
    else:
        return False
n=int(input('Podaj liczbę n: '))
print(liczba_doskonala(n))



