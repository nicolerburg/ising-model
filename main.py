import numpy as np
import math
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# TODO parse user inputs

# Simulation class which is the main body of the simulation
class Simulation():
    def __init__(self):
        self.dynamics = { \
                            "G": self.Glauber, \
                            "K": self.Kawasaki \
                        }

    def Start(self):
        self.GetUserInput()
        self.grid = np.random.choice([-1,1], size=(self.size, self.size))

    def GetUserInput(self):
        self.size = Simulation.ParseInput("Please enter an integer value, N, to specify the size of the lattice.", int)
        self.temp = Simulation.ParseInput("Please enter a temperture value for the simulation.", float)
        self.dynamics_choice = Simulation.ParseInput("Would you like to simulate using Glauber or Kawasaki dynamics? Enter 'G' for Glauber or 'K' for Kawasaki.", str) #maybe can check for keys in dictionary
        self.loops = Simulation.ParseInput("Please enter the amount of loops for the MonteCarlo.", int)

    @staticmethod
    def ParseInput(prompt, type):
        try:
            return type(input(prompt))
        except:
            return Simulation.ParseInput(prompt, type)

    def Display(self):
        figure, self.data_points = Simulation.CreateFigure(self.size)
        self.animation = anim.FuncAnimation(figure, func=self.Animate, frames=self.LoopFunction, interval=10, blit=False, repeat=False)
        plt.show()

    def Animate(self, grid):
        self.data_points.set_data(grid)
        return self.data_points

    @staticmethod
    def CreateFigure(size):
        figure, axes = plt.subplots()
        axes.set_xlabel("X")
        axes.set_ylabel("Y")
        data_points = axes.imshow(np.zeros((size, size)), vmin=-1, vmax=1)
        return figure, data_points

    def LoopFunction(self):
        for i in range(self.loops):
            self.Update()
            yield self.grid

    def Update(self):
        self.dynamics[self.dynamics_choice.capitalize()]()

    def Glauber(self):
        for i in range(self.size**2):
            x = np.random.randint(0,sim.size)
            y = np.random.randint(0,sim.size)
            delta_e = 2 * self.grid[y, x] \
                * (self.grid[(y + 1) % self.size, x] + self.grid[(y - 1)  % self.size, x] \
                + self.grid[y, (x + 1)  % self.size] + self.grid[y, (x - 1)  % self.size])
            if delta_e <= 0 or np.random.rand() <= math.exp(-delta_e/sim.temp):
                self.grid[y, x] *= -1

    def Kawasaki(self):
        pass      
        

sim = Simulation()

sim.Start()
sim.Display()