import random

while True:

    random_Number = random.randint(1, 3)

    if random_Number == 1:

        print('Hello')

    elif random_Number == 2:

        print('Howdy')

    elif random_Number == 3:

        print('Greetings!')

    response = input()

    if response == ('Goodbye'):

        print('Goodbye!')

        break

    else:

        continue
