from World import *


class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world=None):
        """
        Constructor for Game of Life simulator.
        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.
        :return: New state of the world.
        """
        self.generation += 1

        parameters = self.world.get_parameters()

        for x in range(0, self.world.width):
            for y in range(0, self.world.height):
                neighbours = sum(self.world.get_neighbours(x, y))

                if neighbours < min(parameters[0]):
                    # This cell will die due to underpopulation
                    self.world.set(x, y, 0)
                elif neighbours > max(parameters[0]):
                    # This cell will die due to overpopulation
                    self.world.set(x, y, 0)
                elif neighbours in parameters[1]:
                    # This cell came to life (or if it already was alive it will stay alive)
                    self.world.set(x, y, 1)
                elif neighbours in parameters[0]:
                    # This cell survived
                    pass

        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.
        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.
        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.
        :param world: new version of the world.
        """
        self.world = world
