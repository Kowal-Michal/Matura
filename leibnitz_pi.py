
def leibnitz(eps):
    pi=4
    x=0
    i=1
    while abs(x-pi)>=eps:
        x=pi
        if i%2==0:
            pi=pi+4/(2*i+1)
        else:
            pi=pi-4/(2*i+1)
        i+=1
    return pi
eps=float(input('Podaj epsilon: '))
print(leibnitz(eps))