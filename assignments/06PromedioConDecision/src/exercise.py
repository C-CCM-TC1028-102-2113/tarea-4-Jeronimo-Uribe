def main():
    #escribe tu código abajo de esta línea
    print('Introduce la calificación: ')
    calificación=float(input(''))
    total=0
    n=0
    while calificación>0:
        total=total+calificación
        n=n+1
        calificación=float(input(''))
    if calificación<0:
        promedio=total/n
        print(promedio)
        
    pass
if __name__=='__main__':
    main()
