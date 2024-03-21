fizz_buzz = input('Введите число: ')

fizz_buzz = int(fizz_buzz)

for fizz_buzz in range (1, fizz_buzz + 1):
    
    if fizz_buzz % 3 == 0 and fizz_buzz % 5 == 0:
        print('FizzBuzz')

    elif fizz_buzz % 3 == 0:
         print('Fizz')

    elif fizz_buzz % 5 == 0:
         print('Buzz')
    
    else:
        print(fizz_buzz)