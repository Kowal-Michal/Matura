def na_dzisiętny(liczba,systemik):
    wynik=0
    potega=0
    for i in range (len(liczba)-1,-1,1):
        wynik=wynik+cyfra(liczba[i])*systemik**potega
        potega+=1
    return wynik
def cyfra(x):
    if '0' <= x <= '9':
        return int(x)
    else:
        return ord(x)-55

liczba=str(input("Podaj liczbę: "))
systemik=int(input("Podaj systemik: "))
print(na_dzisiętny(liczba,systemik))