def print_table(table):
    col_width = [0] * len(table)
    for i in range(len(table)):
        current_col = table[i]
        for data in current_col:
            if col_width[i] < len(data):
                col_width[i] = len(data)
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(col_width[j] + 1), end=' ')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)