import random

number_Of_Streaks = 0

for experiment_Number in range(10000):

    # Code that creates a list of 100 'heads' or 'tails' values.

    flips = []

    for i in range(100):

        if random.randint(0, 1) == 0:

            flips.append('H')

        else:

            flips.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.

    for i in range(len(flips) - 5):

        if flips[i:i+6] == ['H', 'H', 'H', 'H', 'H', 'H'] or flips[i:i+6] == ['T', 'T', 'T', 'T', 'T', 'T']:

            number_Of_Streaks += 1

            break

print('Chance of streak: %s%%' % (number_Of_Streaks / 100))
