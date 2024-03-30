table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
    col_widths = [0] * len(table)
    count = 0
    while count < len(table):
        for item in table[count]:
            if len(item) > col_widths[count]:
                col_widths[count] = len(item)
        count += 1
    for word in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][word].rjust(col_widths[item]), end=' ')
        print()


print_table(table_data)
