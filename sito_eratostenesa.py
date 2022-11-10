import math
def sito(n):
    if n<2:
        print('Brak liczb pierwszych')
        exit()
    tab=[]
    liczby_pierwsze=[]
    liczby_pierwsze=[True]*(n+1)
    for i in range(2,int(math.sqrt(n))+1):
         if liczby_pierwsze[i]:
             for j in range(2*i,n+1,i):
                 liczby_pierwsze[j]=False
    for i in range(2,n+1):
        if liczby_pierwsze[i]==True:
            tab.append(i)
        else:
            continue
    print(tab)
n=int(input('Podaj ile liczb pierwszych chcesz wyznaczyć:'))
sito(n)
