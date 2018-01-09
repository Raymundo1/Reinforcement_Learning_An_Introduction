#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian
  Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
  Last Modified by: Andrew Jacobsen, Victor Silva, Mohammad M. Ajallooeian, Xinlei Chen
  Last Modified on: 18/9/2017

  Experiment runs 2000 runs, each 1000 steps, of an n-armed bandit problem
"""

# from rl_glue import *  # Required for RL-Glue
from Reinforcement-Learning-An-Introduction.rl_glue import *
# RLGlue("w1_env", "w1_agent")
RLGlue("10_armed_testbed_env", "2_3_agent")

import numpy as np
import sys

 # data: floating point, data_size: integer, filename: string
def save_results(data, data_size, filename):
    with open(filename, "w") as data_file:
        for i in range(data_size):
            data_file.write("{0} ".format(data[0][i]))
            data_file.write("{0}\n".format(data[1][i]))

    
def getOptimalAction():
	return int(RL_env_message("get optimal action"))

# set the value of epsilon and initial_estimate
def set_parameter(setting):
    return RL_agent_message(str(setting))

if __name__ == "__main__":
    num_runs = 2000
    max_steps = 1000
    
    # array to store the results of each step
    optimal_action = np.zeros((2,max_steps))

    for row in [0,1]:
        set_parameter(row)

        print "\nPrinting one dot for every run: {0} total Runs to complete".format(num_runs)
        for k in range(num_runs):
            RL_init()
            
            best_action = getOptimalAction()

            RL_start()
            for i in range(max_steps):
                # RL_step returns (reward, state, action, is_terminal); we need only the
                # action in this problem
                action = RL_step()[2]
                
                if action[0] == best_action:
                    optimal_action[row][i] = optimal_action[row][i] + 1
                

            RL_cleanup()
            print ".",
            sys.stdout.flush()

    save_results(optimal_action / num_runs, max_steps, "RL_EXP_OUT.dat")
    print "\nDone"
