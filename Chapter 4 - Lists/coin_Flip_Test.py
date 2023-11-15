import random

heads_Or_Tails = []

for i in range(100):

    if random.randint(0, 1) == 0:

        heads_Or_Tails.append('H')

    else:

        heads_Or_Tails.append('T')

print(heads_Or_Tails)

length = len(heads_Or_Tails)

print(length)

heads_Streak = ['H', 'H', 'H', 'H', 'H', 'H']

tails_Streak = ['T', 'T', 'T', 'T', 'T', 'T']

number_Of_Streaks = 0

if set(heads_Streak).issubset(heads_Or_Tails):

    number_Of_Streaks = number_Of_Streaks + 1

elif set(tails_Streak).issubset(heads_Or_Tails):

    number_Of_Streaks = number_Of_Streaks + 1

print(number_Of_Streaks)
