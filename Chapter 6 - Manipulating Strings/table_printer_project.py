def print_table(table):
    # Finds max width of each column
    col_width = [0] * len(table)
    for i in range(len(table)):
        for j in range(len(table[i])):
            col_width[j] = max(col_width[j], len(table[i][j]))

    # Prints the table
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(col_width[j] + 1), end=' ')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)