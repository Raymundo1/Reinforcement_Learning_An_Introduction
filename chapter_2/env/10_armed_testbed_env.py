from utils import rand_norm, rand_in_range, rand_un
import numpy as np 

this_reward_observation = (None, None, None)

mean_list = None


def env_init():
	global this_reward_observation
	local_observation = np.zeros(0)
	
	# get reward distribution
	get_reward_distribution()

	this_reward_observation = (0.0, local_observation, False)
	

def get_reward_distribution():
	global mean_list
	
	mean_list = np.zeros(10)
	
	# get the 10 q*(a) 	
	for i in range(10):
		mean_list[i] = rand_norm(0.0, 1.0)


def env_start():
	return this_reward_observation[1]


def env_step(this_action):
	global this_reward_observation

	the_reward = env_get_reward(this_action)

	this_reward_observation = (the_reward, this_reward_observation[1], False)

	return this_reward_observation


def env_get_reward(this_action):
	global mean_list
	
	the_reward = rand_norm(mean_list[int(this_action[0])], 1.0)

	return the_reward

def env_cleanup():
	return


def env_message(inMessage):
	if inMessage == "What is your name?":
		return "My name is skeleton_environment!"
		
	elif inMessage == "get optimal action":
		return np.argmax(mean_list)

	#else
	return "I don't know how to respond to your message"


