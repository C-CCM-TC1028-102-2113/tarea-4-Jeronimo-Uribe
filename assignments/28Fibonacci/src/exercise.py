
def main():
    #escribe tu código abajo de esta línea
    n=int(input('Enter a number: '))
    a=0
    b=1
    i=0
    while i<n:
        suma=a+b
        a=b
        b=suma
        i=i+1
    if i==n:
        print(a)
    pass

if __name__=='__main__':
    main()
