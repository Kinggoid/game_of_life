from unittest import TestCase
from Simulator import *


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()


    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)

    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)

    def test_under_population(self):
        """
        Checks how many neighbours a cel has. If it has less than two, it will die.
        """

        # Make a small world.
        world = World(10, 10)
        self.sim.set_world(world)

        # Create one cell with random coördinates.
        x, y = 2, 5

        self.sim.world.set(x, y)
        self.sim.update()
        self.assertEqual(self.sim.world.get(x, y), 0)

    def test_over_population(self):
        """
        Checks how many neighbours a cel has. If it has less than two, it will die.
        """

        # Make a small world.
        world = World(10, 10)
        self.sim.set_world(world)

        # Create a cell and a few surrounding neighbours
        coordinates = [[2,5], [3,5], [1,5], [2,6], [2,7]]

        for cell in coordinates:
            self.sim.world.set(cell[0], cell[1])

        self.sim.update()
        self.assertEqual(self.sim.world.get(2, 5), 0)

    def test_survival_2_neighbours(self):
        """
        Checks how many neighbours a cel has. If it has two or three neighbours it will live.
        """

        # Make a small world.
        world = World(10, 10)
        self.sim.set_world(world)

        # Create a cell and a few surrounding neighbours
        coordinates = [[2, 5], [3, 5], [2, 6], [3, 6]]

        for cell in coordinates:
            self.sim.world.set(cell[0], cell[1])

        self.sim.update()
        self.assertEqual(self.sim.world.get(2, 5), 1)

    def test_survival_3_neighbours(self):
        """
        Checks how many neighbours a cel has. If it has two or three neighbours it will live.
        """

        # Make a small world.
        world = World(10, 10)
        self.sim.set_world(world)

        # Create a cell and a few surrounding neighbours
        coordinates = [[2, 5], [3, 5], [1, 5], [2, 6]]

        for cell in coordinates:
            self.sim.world.set(cell[0], cell[1])

        self.sim.update()
        self.assertEqual(self.sim.world.get(2, 5), 1)

    def test_birth_population(self):
        """
        Checks how many neighbours a dead cel has. If it is exactly three, it will come to life.
        """

        # Make a small world.
        world = World(10, 10)
        self.sim.set_world(world)

        # The coördinates of the dead cell we will focus on are [3, 4]
        # Create a few cells
        coordinates = [[3, 5], [3, 3], [2, 4]]

        for cell in coordinates:
            self.sim.world.set(cell[0], cell[1])

        self.sim.update()
        self.assertEqual(self.sim.world.get(3, 4), 1)

    def test_change_parameters(self):
        """
        If you dont do anything you will get the basic game of life rules, but if you want you can change the
        parameters for a different ruleset.
        """

        # Make a small world.
        world = World(10, 10)
        self.sim.set_world(world)

        self.sim.world.set_parameters(1, 2, 2)

        self.assertEqual(self.sim.world.getP(), [1, 2, 2])
