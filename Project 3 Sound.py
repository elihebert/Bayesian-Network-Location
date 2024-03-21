from decimal import Decimal
from grid import Grid
from m1_m2 import M1, M2
from current_position import Current_Position
class Sound: 
    def __init__(self, grid):
        #initialize nested dictionary to store probability distributions of sound based on location
        self.distribution = {}

        #cretae empty dictionary (with its sound distribution) for each cell in grid
        for x in range(grid.get_rows()):
            for y in range(grid.get_columns()):
                self.distribution[((x, y))] = {}

        #populate sound distribution for each cell based on distance
        for i, j in self.distribution.items():
            #probability of sound being reported at the same location
            j.update({i: Decimal(0.6)})

            #locations one step away from current location
            one_step_away1 = grid.one_step_away(i)
            #probabilities of sound being reported at spots one step away; divided by number of those locations
            for y in one_step_away1:
                j.update({y: Decimal(0.3 / len(one_step_away1))})

            #locations two steps away from current location
            two_steps_away1 = grid.two_steps_away(i)
            #probabilities of sound being reported at spots two steps away; divided by number of those locations
            for y in two_steps_away1:
                j.update({y: Decimal(0.1 / len(two_steps_away1))})

    def generate_probability(self, current_position, sound_position):
        #return probability of a sound being reported at sound_position given that the monkey is at current_position
        #if sound_position is not in distribution for current_position, return 0
        if sound_position in self.distribution[current_position]:
            probability = self.distribution[current_position][sound_position]
        else:
            probability = Decimal(0)
        return probability
    
    def print_distribution(self):
        print("Sound distribution:")
        for x, y in self.distribution.items():
            print(f"Current location: ({x[0]}, {x[1]})")
            for a, b in y.items():
                print(f"Sound reported at: ({a[0]}, {a[1]}), Probability: {b:.8f}")