from decimal import Decimal
from collections import defaultdict
from grid import Grid
from current_position import Current_Position

#motion sensor placed at top-left
class M1:
    def __init__(self, grid):
        #initialize probability distribution for motion detection; varying on proximity ot sensor
        self.distribution = {}
        for x in range(grid.get_rows()):
            for y in range(grid.get_columns()):
                #if on top or left edges, compute true positive rate based on distance from sensor
                if (x == 0 or y == 0):
                    true_pos = Decimal(0.9 - 0.1 * (x + y))
                    false_pos = Decimal(1 - true_pos)
                else:
                    #if not set default low true positive rate
                    true_pos = Decimal(0.05)
                    false_pos = Decimal(0.95)
                self.distribution[((x, y))] = (true_pos, false_pos)

    def generate_probability(self, current_position, motion):
        #get probability of motion detection at current_position
        probability = self.distribution[current_position];
        return probability[0] if motion else probability[1]

    def print_distribution(self):
        #print probability distribution for motion sensor
        print("Motion sensor #1 (top left) distribution:")
        for x, y in self.distribution.items():
            print(f"Current location: ({x[0]}, {x[1]}), True probability: {y[0]:.8f}, False probability: {y[1]:.8f}")

#motion sensor placed at bottom-right
class M2:
    def __init__(self, grid):
        #initialize probability distribution for motion detection; varying on proximity ot sensor
        self.distribution = {}
        rows = grid.get_rows()
        columns = grid.get_columns()
        for x in range(rows):
            for y in range(columns):
                #if on bottom or right edges, compute true positive rate based on distance from sensor
                if (x == rows-1 or y == columns - 1):
                    if x == rows-1:
                        separation = columns-1 - y
                    else:
                        separation = rows-1 - x
                    true_pos = Decimal(0.9 - 0.1 * separation)
                    false_pos = Decimal(1 - true_pos)
                else:
                    #if not set default low true positive rate
                    true_pos = Decimal(0.05)
                    false_pos = Decimal(0.95)
                self.distribution[((x, y))] = (true_pos, false_pos)

    def generate_probability(self, current_position, motion):
        #get probability of motion detection at current_position
        probability = self.distribution[current_position];
        return probability[0] if motion else probability[1]
    
    def print_distribution(self):
        print("Motion sensor #2 (bottom right) distribution:")
        for x, y in self.distribution.items():
            print(f"Current location: ({x[0]}, {x[1]}), True probability: {y[0]:.8f}, False probability: {y[1]:.8f}")