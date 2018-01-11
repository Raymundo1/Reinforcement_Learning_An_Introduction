"""
	Author: Xinlei Chen
"""
import sys
sys.path.insert(0, '../../tool')
sys.path.insert(0, '../env') 


from rl_glue import *  # Required for RL-Glue
import matplotlib.pyplot as plt


episode_num = 200
max_steps = 10000

RLGlue("wind_env", "6_4_agent")

time_steps = 0
time_steps_record_1 = [0]
episode_record_1 = [0]
optimal_policy_step_num = 20 # step num under optimal policy for 8 actions

RL_init()
for i in range(episode_num):
	RL_episode(max_steps)
	time_steps = time_steps + RL_num_steps()
	time_steps_record_1.append(time_steps)
	episode_record_1.append(i+1)

	if RL_num_steps() < optimal_policy_step_num:
		optimal_policy_step_num = RL_num_steps()

print "num of step under optimal policy [4 actions] = ", optimal_policy_step_num

plt.plot(time_steps_record_1, episode_record_1, 'b')
plt.xlabel('Time steps')
plt.ylabel('Episodes')
plt.savefig("figure_6_4.pdf")
