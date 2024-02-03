while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('===' * 10)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('===' * 10)
print('PROGRAMA TABUADA FINALIZADO!')
