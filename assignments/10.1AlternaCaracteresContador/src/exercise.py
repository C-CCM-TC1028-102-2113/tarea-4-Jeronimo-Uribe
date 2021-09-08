def main():
    #escribe tu código abajo de esta línea
    n=int(input('Dame un número entero: '))
    num=1
    while num<n:
        if num%2==0:
            print(str(num)+('-%'))
            num=num+1
        elif num%2!=0:
            print(str(num)+('-#'))
            num=num+1
    if num==n:
        if num%2==0:
            print(str(num)+('-%'))
        elif num%2!=0:
            print(str(num)+('-#')) 
    
    pass

if __name__=='__main__':   
    main()
