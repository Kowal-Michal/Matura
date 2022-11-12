
def leibnitz(eps):
    p1=0
    p2=0
    i=1
    while abs(p2-p1)<=eps:
        p1=(-1)**i/2*i+1
        p2=(-1)**(i-1)/2*(i-1)+1
        i+=1
    return p1*4
eps=float(input('Podaj epsilon: '))
print(leibnitz(eps))

