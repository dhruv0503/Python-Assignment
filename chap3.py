def collatz(number):
    if number == 1:
        print('Collatz Complete. Amazing isn\'t it!')
    elif number % 2 == 0:
        print(int(number / 2))
        collatz(number / 2)
    else:
        print(int(number * 3 + 1))
        collatz(number * 3 + 1)


try:
    collatz(int(input('Choose any integer greater than 1: ')))
except ValueError:
    print('Non-Integer entered, program will exit')
