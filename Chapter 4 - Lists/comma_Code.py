spam = ['apples', 'bananas', 'tofu', 'cats']

def comma():

    last = len(spam) - 1

    for i in spam[:last]:

        print(i, end=', ')

    print('and ' + spam[last] + '.')

comma()
