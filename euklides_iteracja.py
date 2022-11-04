def euk_it(a,b):
    pom=0
    while b!=0:
        pom=b
        b=a%b
        a=pom
    return a
a=int(input("Podaj liczbę 1: "))
b=int(input("Podaj liczbę 2: "))
print(euk_it(a,b))