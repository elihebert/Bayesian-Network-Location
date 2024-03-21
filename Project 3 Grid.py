from decimal import Decimal
from collections import defaultdict

class Grid:
    def __init__(self, row, column):
        #initialize grid with given rows and columns; set initial unfiform distribution for each cell
        self.row = row
        self.column = column
        self.distribution = [[Decimal(1/(row*column)) for col_index in range(column)] for row_index in range(row)]

    def get_rows(self):
        #return number of rows
        return self.row
    
    def get_columns(self):
        #return number of columns
        return self.column
    
    def shift_prob(self, row, column, val):
        #modify probability distribution of specific cell
        self.distribution[row][column] = val

    def normalize(self):
        #normalize probability distribution to sum to 1
        res = Decimal(0)
        for row in self.distribution:
            for col in row:
                res += col
        for row in range(self.row):
            for col in range(self.column):
                self.distribution[row][col] /= res

    def generate_locations(self):
        #get list of all possible locations in grid
        return [(row, column) for row in range(self.row) for column in range(self.column)]
    
    def one_step_away(self, loc):
        #return list of valid locations that are one step away from given location
        row, column = loc[0], loc[1]
        location_list = []
        if (self.is_valid_location((row + 1, column))):
            location_list.append((row + 1, column))
        if (self.is_valid_location((row - 1, column))):
            location_list.append((row - 1, column))
        if (self.is_valid_location((row, column + 1))):
            location_list.append((row, column + 1))
        if (self.is_valid_location((row, column - 1))):
            location_list.append((row, column - 1))
        return location_list
    
    def two_steps_away(self, loc):
        #return list of valid locations that are two steps away from given location
        row, column = loc[0], loc[1]
        location_list = []
        if (self.is_valid_location((row + 2, column))):
            location_list.append((row + 2, column))
        if (self.is_valid_location((row - 2, column))):
            location_list.append((row - 2, column))
        if (self.is_valid_location((row, column + 2))):
            location_list.append((row, column + 2))
        if (self.is_valid_location((row, column - 2))):
            location_list.append((row, column - 2))
        return location_list
    
    def is_valid_location(self, loc):
        #check if given location is valid
        row, column = loc[0], loc[1]
        return 0 <= row < self.row and 0 <= column < self.column
    
    def output_distribution(self):
        #print probability distribution for grid
        for row in self.distribution:
            print("  ", end = "")
            for col in row:
                print(f"{col:.8f}", end = " ")
            print("")
        print("")

    def output_distribution_plus_location(self):
        #print probability distribution for grid 
        print("Last location distribution:")
        for x in range(self.row):
            for y in range(self.column):
                print(f"Last location: ({x}, {y}), probability: {self.distribution[x][y]:.8f}")

    