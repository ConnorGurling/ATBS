# Conway's Game of Life

import random, time, copy

WIDTH = 60

HEIGHT = 20

# Create a list of list for the cells:

next_Cells = []

for x in range(WIDTH):

    column = []  # Create a new column

    for y in range(HEIGHT):

        if random.randint(0, 1) == 0:

            column.append('#')  # Add a living cell.

        else:

            column.append(' ')  # Add a dead cell.

    next_Cells.append(column)  # next_Cells is a list of column lists.

while True:  # Main program loop.

    print('\n\n\n\n\n')  # Separate each step with newlines.

    current_Cells = copy.deepcopy(next_Cells)

    # Print current_Cells on the screen:

    for y in range(HEIGHT):

        for x in range(WIDTH):

            print(current_Cells[x][y], end=' ')  # Print the # or space.

        print()  # Print a newline at the end of the row.

    # Calculate the next step's cells based on current step's cells:

    for x in range(WIDTH):

        for y in range(HEIGHT):

            # Get neighboring coordinates:

            # '% WIDTH' ensures left_Coord is always between 0 and WIDTH - 1

            left_Coord = (x - 1) % WIDTH

            right_Coord = (x + 1) % WIDTH

            above_Coord = (y - 1) % HEIGHT

            below_Coord = (y + 1) % HEIGHT

            # Count number of living neighbors:

            num_Neighbors = 0

            if current_Cells[left_Coord][above_Coord] == '#':

                num_Neighbors += 1  # Top-left neighbor is alive

            if current_Cells[x][above_Coord] == '#':

                num_Neighbors += 1  # Top neighbor is alive

            if current_Cells[right_Coord][above_Coord] == '#':

                num_Neighbors += 1  # Top-right neighbor is alive.

            if current_Cells[left_Coord][y] == '#':

                num_Neighbors += 1  # left neighbor is alive.

            if current_Cells[right_Coord][y] == '#':

                num_Neighbors += 1  # Right neighbor is alive.

            if current_Cells[left_Coord][below_Coord] == '#':

                num_Neighbors += 1  # Bottom-left neighbor is alive.

            if current_Cells[x][below_Coord] == '#':

                num_Neighbors += 1  # Bottom neighbor is alive.

            if current_Cells[right_Coord][below_Coord] == '#':

                num_Neighbors += 1  # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:

            if current_Cells[x][y] == '#' and (num_Neighbors == 2 or num_Neighbors == 3):

                # Living cells with 2 or 3 neighbors stay alive:

                next_Cells[x][y] = '#'

            elif current_Cells[x][y] == ' ' and num_Neighbors == 3:

                # Dead cells with 3 neighbors become alive:

                next_Cells[x][y] = '#'

            else:

                # Everything else dies or stays dead:

                next_Cells[x][y] = ' '

            time.sleep  # Add a 1-second pause to reduce flickering.
