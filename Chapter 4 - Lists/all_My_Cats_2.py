cat_Names = []

while True:

    print('Enter the name of cat ' + str(len(cat_Names) + 1) +

        ' (Or enter nothing to stop.):')

    name = input()

    if name == '':

        break

    cat_Names = cat_Names + [name]  # list concatenation

print('The cat names are:')

for name in cat_Names:

    print(' ' + name)
