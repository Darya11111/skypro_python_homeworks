x = int(input('Введите сумму взноса: '))
y = int(input('На сколько лет: '))

def bank(x, y):

    for i in range(y):
        x = (x * 1.1)
    return(x)
result = bank(x, y)
        
print(f'При взносе {x} руб., Сумма за {y} год/лет, составит {result} руб.')