from utils import rand_in_range
import numpy as np 

last_action = None

# initial esitamte
Q_a = None  # NumPy array
alpha = None
epsilon = None

num_actions = 10

setting = None


def agent_init():
	global last_action, Q_a, N_a, alpha, epsilon

	last_action = np.zeros(1)
	
	alpha = np.array([0.1])	
	
	if setting == 0:
		# first setting (setting = 0)
		Q_a = np.zeros(10) + 5
		epsilon = 0

	else:
		# second setting (setting = 1)
		Q_a = np.zeros(10)
		epsilon = 0.1
	

def agent_start(this_observation):
	global last_action

	# step = 1, exploration
	# local_action = np.zeros(1)
	# # [0, num_actions)
	# local_action[0] = rand_in_range(num_actions)
	# last_action = local_action

	last_action[0] = rand_in_range(num_actions)

	# return local_action[0]
	return last_action


def action_select():
	# 0 represent exploration, 1 represent exploitation
	choice = np.array([0,1])
	result = np.random.choice(choice, p=[epsilon, 1-epsilon])


	if result == 0:
		# exploration
		# print "exploration"
		return rand_in_range(num_actions)
 
	else:
		# exploitation
		# print "exploitation"
		return np.argmax(Q_a)


def update_estimate(reward):
	global last_action, Q_a

	action = int(last_action)
	Q_a[action] = Q_a[action] + (alpha[0] * (reward - Q_a[action]))



def agent_step(reward, this_observation):
	global last_action

	# (1) perform a learning update to the Q-values based 
	# on the reward received as input to agent_step function 
	# and the action the agent took on the previous time step 
	update_estimate(reward)


	# (2) return a new action based on the updated Q-values
	# local_action = np.zeros(1)
	# local_action[0] = action_select()
	# last_action = local_action
	last_action[0] = action_select()

	return last_action


def agent_end(reward):
	pass


def agent_cleanup():
	pass


def agent_message(inMessage):
	global setting
	if inMessage == "What is your name?":
		return "My name is skeleton_agent!"

	elif inMessage == "0":
		setting = 0

	elif inMessage == "1":
		setting = 1

	# else
	return "I don't know how to respond to your message"