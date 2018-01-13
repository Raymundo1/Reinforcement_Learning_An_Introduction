"""
	Author: Xinlei Chen
"""
import sys
sys.path.insert(0, '../../tool')
sys.path.insert(0, '../env')


from rl_glue import * # Required for RL_Glue
import matplotlib.pyplot as plt 
import numpy as np 

RLGlue("gridworld_env", "Dyna_Q_agent")

num_runs = 10
num_episode = 50
max_steps = 10000

# for the seed control
one_circle = 0
# rand = np.random.RandomState(0)
rand = np.random.RandomState()


tem_input_template = "set n = "
order = [(0, 0), (1, 5), (2, 50)]
result = np.zeros((3, num_episode))

for run in range(num_runs):
	for row_index, planning_steps in order:

		set_para = tem_input_template + str(planning_steps)
		RL_agent_message(set_para)
		
		time_steps = np.zeros(num_episode)
		
		RL_init()

		for episode in range(num_episode):

			if(episode == 0):
				if(one_circle == 0):
					rand_seed = rand.choice(range(100))

				np.random.seed(rand_seed)
				one_circle += 1

				# one round finish
				if(one_circle == 3):
					one_circle = 0

			RL_episode(max_steps)
			time_steps[episode] = RL_num_steps()

			if(episode == 0):
				print "Episode[1]'s step = ", RL_num_steps()
				print("\n")


		result[row_index, :] = result[row_index, :] + time_steps

result = result / num_runs


# 2 - 50
x_axis = [x+2 for x in range(num_episode-1)]
plt.plot(x_axis, result[0, 1:], color='b', label='n = 0')
plt.plot(x_axis, result[1, 1:], color='r', label='n = 5')
plt.plot(x_axis, result[2, 1:], color='g', label='n = 50')
plt.legend(loc=1, borderaxespad=0.)
plt.xlabel('Episodes')
plt.ylabel('Steps per episode')
plt.savefig("figure_8_3.pdf")

# 1 - 50
# x_axis = [x+1 for x in range(num_episode)]
# plt.plot(x_axis, result[0, :], 'b')
# plt.plot(x_axis, result[1, :], 'r')
# plt.plot(x_axis, result[2, :], 'g')
# plt.xlabel('Episodes')
# plt.ylabel('Steps per episode')
# plt.show()

