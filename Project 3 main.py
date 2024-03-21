
from grid import Grid
from m1_m2 import M1, M2
from current_position import Current_Position
from sound import Sound
from decimal import Decimal
def main():
    #get file name; check if debug is wanted
    file = input("Enter the name of the file: ")
    debug = True if input("Enter 'd' for debug mode: ") == 'd' else False
    print()

    #read input from prevoiusly specified file
    text = open(file, "r")
    location = text.readline().split()
    rows = int(location[0])
    columns = int(location[1])

    #initialize grid, current position, motion 1, motion 2, and sound
    grid = Grid(rows, columns)
    current_position = Current_Position(grid)
    motion_1 = M1(grid)
    motion_2 = M2(grid)
    sound = Sound(grid)
    if debug:
        grid.output_distribution()
        current_position.print_distribution()
        motion_1.print_distribution()
        motion_2.print_distribution()
        sound.print_distribution()
        print()
    step = 0
    print("Initial distribution of monkey's last location:")
    grid.output_distribution()

    #process the obersevations from the file
    while True:
        line = text.readline()
        if line == "":
            break
        else:
            observations = line.split()
            motion1 = True if observations[0] == "1" else False
            motion2 = True if observations[1] == "1" else False
            sound1 = (int(observations[2]), int(observations[3]))
            #observations displayed
            print(f"Observation: Motion1: {'True' if motion1 else 'False'}, Motion2: {'True' if motion2 else 'False'}, Sound location: ({sound1[0]}, {sound1[1]})")
            print(f"Monkey's predicted current location at time step: {step}")
            step += 1
            final_probability = {}

            #calculate probability of the monkey being at each location
            for x in grid.generate_locations():
                #(x[0], x[1]) is the current location
                probability_current_location = Decimal(0)
                if debug:
                    print(f"   Calculating total probability for current location: ({x[0]}, {x[1]})")
                for y in grid.generate_locations():
                    #(y[0], y[1]) is the last location
                    probability_y = grid.distribution[y[0]][y[1]]
                    probability_c_given_y = current_position.generate_probability(y, x) ##this might be where i am going wrong
                    probability_motion1_given_c = motion_1.generate_probability(x, motion1)
                    probability_motion2_given_c = motion_2.generate_probability(x, motion2)
                    probability_sound_given_c = sound.generate_probability(x, sound1)
                    if debug:
                        print(f"   Probs being multiplied for last location: ({y[0]}, {y[1]}): {float(probability_y):.8f}, {float(probability_c_given_y):.8f}, {float(probability_motion1_given_c):.8f}, {float(probability_motion2_given_c):.8f}, {float(probability_sound_given_c):.8f}")

                    #update total probability for current location
                    probability_current_location += probability_y * probability_c_given_y * probability_motion1_given_c * probability_motion2_given_c * probability_sound_given_c
                final_probability.update({x: probability_current_location})

            #update the grid with the new probabilities
            for x in grid.generate_locations():
                grid.shift_prob(x[0], x[1], final_probability[x])
            if debug:
                print()
                print("Before normalization:")
                grid.output_distribution()
                grid.normalize()
                print()
                print("After normalization:")
                grid.output_distribution()
            else:
                grid.normalize()
                grid.output_distribution()
main()


        
