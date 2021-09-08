

def main():
    #Escribe tu código debajo de esta línea
    n=int(input('Escribe un número entero: '))
    num=1
    while num**2<n:
        num=num+1
    if num**2>=n:
        print(num)
    
    pass

if __name__=='__main__':
    main()
