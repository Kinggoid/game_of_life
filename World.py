from Visualisation import *
from Simulator import *
import time

# Configuratie
VISUALISATION=True

if __name__ == "__main__":
    w = World(110)
    sim = Simulator(w)

    change_parameters = input(
        'Do you wanna change the parameters? Right now we are using the standard B3/S23 rules. (Y/N): ')
    if change_parameters == 'Y' or 'y':
        survived = []
        birthed = []
        while True:
            survive = input(
                'What number of neighbours do you want a cell to have in order to surive? (name one number): ')
            continuee = input('Do you want to add another number?: ')
            if type(survive) != int and 0 <= int(survive) <= 8:
                survived.append(int(survive))
            if continuee != 'Y' and continuee != 'y':
                break

        while True:
            birth = input(
                'What number of neighbours do you want a dead cell to have in order to become alive? (name one number): ')
            continuee = input('Do you want to add another number?: ')
            if type(birth) != int and 0 <= int(birth) <= 8:
                birthed.append(int(birth))
            if continuee != 'Y' and continuee != 'y':
                break

        sim.world.set_parameters(survived, birthed)

    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(0.5)
