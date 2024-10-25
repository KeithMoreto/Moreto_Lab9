#print the number of rows for the right-angled triangle
num_rows =int(input('Enter The number of rows: '))

current_number = 1 #start from 1
triangle_row = ''


for row in range(1, num_rows + 1): #rows

    for column in range(row): #columns

      triangle_row += str(current_number) + ' ' # Adds columns

      current_number += 1 # Adds value to next number

    print(triangle_row) # Displays a row

    triangle_row = '' #row reset
