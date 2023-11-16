theBoard = {'1a': 'brook', '1b': 'bknig', '1c': 'bbish', '1d': 'bquee', '1e': 'bking', '1f': 'bbish', '1g': 'bknig', '1h': 'brook',
            '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
            '3a': '     ', '3b': '     ', '3c': '     ', '3d': '     ', '3e': '     ', '3f': '     ', '3g': '     ', '3h': '     ',
            '4a': '     ', '4b': '     ', '4c': '     ', '4d': '     ', '4e': '     ', '4f': '     ', '4g': '     ', '4h': '     ',
            '5a': '     ', '5b': '     ', '5c': '     ', '5d': '     ', '5e': '     ', '5f': '     ', '5g': '     ', '5h': '     ',
            '6a': '     ', '6b': '     ', '6c': '     ', '6d': '     ', '6e': '     ', '6f': '     ', '6g': '     ', '6h': '     ',
            '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
            '8a': 'wrook', '8b': 'wknig', '8c': 'wbish', '8d': 'wking', '8e': 'wquee', '8f': 'wbish', '8g': 'wknig', '8h': 'wrook',}

def printBoard(board):

    print('    a     b     c     d     e     f     g     h')

    print('1 ' + board['1a'] + '|' + board['1b'] + '|' + board['1c'] + '|' + board['1d'] + '|' + board['1e'] + '|' + board['1f'] + '|' + board['1g'] + '|' + board['1h'])

    print('  -----+-----+-----+-----+-----+-----+-----+-----')

    print('2 ' + board['2a'] + '|' + board['2b'] + '|' + board['2c'] + '|' + board['2d'] + '|' + board['2e'] + '|' + board['2f'] + '|' + board['2g'] + '|' + board['2h'])

    print('  -----+-----+-----+-----+-----+-----+-----+-----')

    print('3 ' + board['3a'] + '|' + board['3b'] + '|' + board['3c'] + '|' + board['3d'] + '|' + board['3e'] + '|' + board['3f'] + '|' + board['3g'] + '|' + board['3h'])

    print('  -----+-----+-----+-----+-----+-----+-----+-----')

    print('4 ' + board['4a'] + '|' + board['4b'] + '|' + board['4c'] + '|' + board['4d'] + '|' + board['4e'] + '|' + board['4f'] + '|' + board['4g'] + '|' + board['4h'])

    print('  -----+-----+-----+-----+-----+-----+-----+-----')

    print('5 ' + board['5a'] + '|' + board['5b'] + '|' + board['5c'] + '|' + board['5d'] + '|' + board['5e'] + '|' + board['5f'] + '|' + board['5g'] + '|' + board['5h'])

    print('  -----+-----+-----+-----+-----+-----+-----+-----')

    print('6 ' + board['6a'] + '|' + board['6b'] + '|' + board['6c'] + '|' + board['6d'] + '|' + board['6e'] + '|' + board['6f'] + '|' + board['6g'] + '|' + board['6h'])

    print('  -----+-----+-----+-----+-----+-----+-----+-----')

    print('7 ' + board['7a'] + '|' + board['7b'] + '|' + board['7c'] + '|' + board['7d'] + '|' + board['7e'] + '|' + board['7f'] + '|' + board['7g'] + '|' + board['7h'])

    print('  -----+-----+-----+-----+-----+-----+-----+-----')

    print('8 ' + board['8a'] + '|' + board['8b'] + '|' + board['8c'] + '|' + board['8d'] + '|' + board['8e'] + '|' + board['8f'] + '|' + board['8g'] + '|' + board['8h'])

def validMove():

    while True:

        print('Turn for ' + turn + '. What is the location of the piece you would like to move?')

        oldCoord = str(input())

        if oldCoord in theBoard.keys() and theBoard[oldCoord].startswith(prefix):

            while True:

                print('Where would you like to move it?')

                newCoord = str(input())

                if newCoord in theBoard.keys():

                    theBoard[newCoord] = theBoard[oldCoord]

                    theBoard[oldCoord] = '     '

                    break

                else:

                    print('Invalid move, please try again')

            break

        else:

            print('Invalid move, please try again')

def win_Condition():

    if all(value.startswith(prefix) or value.startswith(' ') for value in theBoard.values()):

        print(turn + ' has won, congratulations!')

        exit

turn = 'White'

prefix = 'w'

win = 'false'

while True:

    printBoard(theBoard)

    validMove()

    win_Condition()

    if turn == 'White':

        turn = 'Black'

        prefix = 'b'

    else:

        turn = 'White'

        prefix = 'w'
