import random

def get_Answer(answer_Number):

    if answer_Number == 1:

        return 'It is certain'

    elif answer_Number == 2:

        return 'It is decidedly so'

    elif answer_Number == 3:

        return 'Yes'

    elif answer_Number == 4:

        return 'Reply hazy try again'

    elif answer_Number == 5:

        return 'Ask again later'

    elif answer_Number == 6:

        return 'Concentrate and ask again'

    elif answer_Number == 7:

        return 'My reply is no'

    elif answer_Number == 8:

        return 'Outlook not so good'

    elif answer_Number == 9:

        return 'Very doubtful'


r = random.randint(1, 9)

fortune = get_Answer(r)

print(fortune)
