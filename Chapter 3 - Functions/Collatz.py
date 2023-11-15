def collatz(number):

    if number % 2 == 0:

        result = number // 2

        print(result)

        return result

    else:

        result = 3 * number + 1

        print(result)

        return result


def user_Input():

    while True:

        try:

            print('Please type a number:')

            number = int(input())

            break

        except ValueError:

            print('You MUST enter an interger.')

    while number != 1:

        number = collatz(number)

    print('Reached 1!')


user_Input()
