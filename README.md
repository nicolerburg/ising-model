# ising-model
 This program simulates the Ising Model using a Monte Carlo algorithm.

 It consists of a N by N lattice of spins either spin-up (1) or spin-down (-1) 
 which are changed over time using a Markov Chain and the Metropolis Test.

 When running the code you have a choice to run a live visualization of the
 lattice's spin state over time at a certain temperature or collect data points over a range of temperatures (1 to 3).

 To make this choice simply run the code calling sim.Start()
 and answer the prompts in the console.

 The data collection can be set to run with either Glauber or Kawasaki Dynamics. 

 The program files also contain jsonc data files which can be used to graph previously collected results
 by removing the sim.Start() function call and instead calling the PlotData() function. 
 
 # Please ensure that the sim.json_path variable matches the file path and name of the data you wish to plot.

# Runtimes:
    Glauber: 35 minutes for 21 temperatures of 10000 sweeps each
    Kawasaki: 105 minutes for 21 temperatures of 10000 sweeps each
