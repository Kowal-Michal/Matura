def euk_rek(a,b):
    if b!=0:
        return euk_rek(b,a%b)
    return a
a=int(input('Podaj liczbe 1: '))
b=int(input('Podaj liczbe 2: '))
print(euk_rek(a,b))