my_Pets = ['Zophie', 'Pooka', 'Fat-tail']

print('Enter a pet name:')

name = input()

if name not in my_Pets:

    print('I do not have a pet named' + name)

else:

    print(name + ' is my pet.')
