import random, sys

print('ROCK, PAPER, SCISSORS')

# These varliables keep track of the number of wins, losses and ties.

wins = 0

losses = 0

ties = 0

while True: # The main game loop.

    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    while True: # The player input loop.

        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

        player_Move = input()

        if player_Move == 'q':

            sys.exit() #Quit the program.

        if player_Move == 'r' or player_Move == 'p' or player_Move == 's':

            break # Break our of the player input loop.

        print('Type one of r, p, s, or q.')


    # Display what the player chose:

    if player_Move == 'r':

        print('ROCK versus...')

    elif player_Move == 'p':

        print('PAPER verus...')

    elif player_Move == 's':

        print('SCISSORS versus...')


    # Display what the computer chose:

    random_Number = random.randint(1, 3)

    if random_Number == 1:

        computer_Move = 'r'

        print('ROCK')

    elif random_Number == 2:

        computer_Move = 'p'

        print('PAPER')

    elif random_Number == 3:

        computer_Move = 's'

        print('SCISSORS')


    # Display and record the win/loss/tie:

    if player_Move == computer_Move:

        print('It is a tie!')

        ties = ties + 1

    elif player_Move == 'r' and computer_Move == 's':

        print('You win!')

        wins = wins + 1

    elif player_Move == 'p' and computer_Move == 'r':

        print('You win!')

        wins = wins + 1

    elif player_Move == 's' and computer_Move == 'p':

        print ('You win!')

        wins = wins + 1

    elif player_Move == 'r' and computer_Move == 'p':

        print('You lose!')

        losses = losses + 1

    elif player_Move == 'p' and computer_Move == 's':

        print('You lose!')

        losses = losses + 1

    elif player_Move == 's' and computer_Move == 'r':

        print('You lose!')

        losses = losses + 1
