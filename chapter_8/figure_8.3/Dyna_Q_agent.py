"""
	Author: Xinlei Chen
	Dyna-Q agent [4 actions]
"""

import numpy as np

num_actions = 4
last_action = None
last_state = None


# this rand seed for model choice
rand = np.random.RandomState(0)

# Basic arguments
epsilon = 0.1
alpha = 0.1
gamma = 0.95

# number of model update times [default]
n = 50

# value function && model
Q = None
Model = None


def agent_init():
	global last_action, last_state, Q, Model
	
	last_state = np.array([0, 0])
	last_action = 0

	Q = np.zeros((6, 9, num_actions))

	Model = dict()


def agent_start(state):
	"""
	Arguments: states: numpy array
	Returns: action: integer
	"""
	global last_action, last_state

	# 0 represent exploration, 1 represent explotation
	choice = np.array([0, 1])

	result = np.random.choice(choice, p=[epsilon, 1-epsilon])

	if result == 0:
		# exploration
		action = np.random.choice(range(4))

	else:
		# exploitation
		action = find_max_argument(state)

	last_action = action
	last_state = state

	return action


def agent_step(reward, state):
	"""
	Arguments: reward: floating point, state: integer
	Returns: action: integer
	"""
	global Q, last_action, last_state, Model

	Q[last_state[0], last_state[1], last_action] = Q[last_state[0], last_state[1], last_action] + \
		alpha*(reward + (gamma * np.amax(Q[state[0], state[1], :])) - Q[last_state[0], last_state[1], last_action])


	##### next action selection ######
	# 0 represent exploration, 1 represent explotation
	choice = np.array([0, 1])

	result = np.random.choice(choice, p=[epsilon, 1-epsilon])

	if result == 0:
		# exploration
		action = np.random.choice(range(4))

	else:
		# exploitation
		action = find_max_argument(state)

	##################################

	##### update model ###############
	if tuple(last_state) not in Model.keys():
		Model[tuple(last_state)] = dict()

	# maybe has bug #####
	Model[tuple(last_state)][last_action] = [reward, state]
	##################################

	##### use sample model to update Q #####
	sample_model_update_Q(n)
	########################################

	last_state = state
	last_action = action

	return action


def agent_end(reward):
	"""
	Arguments: reward: floating point
	Returns: Nothing
	"""
	global Q, Model
	Q[last_state[0], last_state[1], last_action] = Q[last_state[0], last_state[1], last_action] + \
		alpha*(reward - Q[last_state[0], last_state[1], last_action])



def agent_cleanup():
	"""
	This function is not used
	"""
	return


def agent_message(in_message):
	"""
	Arguments
	---------
	inMessage : string
		the message being passed

	Returns
	-------
	string : the response to the message
	"""
	global n, alpha

	piece = in_message.split()

	if(piece[1] == "n"):
		n = int(piece[3])
		print "Successfully set n to ", n

	if(piece[1] == "alpha"):
		alpha = float(piece[3])
		print "Successfully set alpha to ", alpha

	return "I don't know how to respond to your message"


def sample_model_update_Q(times):
	if(len(Model.keys()) > 0):
		for i in range(times):
			stateIndex_select = rand.choice(range(len(Model.keys())))
			state_select = list(Model)[stateIndex_select]
			actionIndex_select = rand.choice(range(len(Model[state_select].keys())))
			action_select = list(Model[state_select])[actionIndex_select]
			
			(simu_reward, simu_state) = Model[state_select][action_select]
			Q[state_select[0], state_select[1], action_select] = Q[state_select[0], state_select[1], action_select] + \
				alpha*(simu_reward + (gamma * np.amax(Q[simu_state[0], simu_state[1], :])) - Q[state_select[0], state_select[1], action_select])


def find_max_argument(state):
	if(all(x == Q[state[0], state[1], 0] for x in Q[state[0], state[1], :])):
		action = np.random.choice(range(4))

	else:
		action = np.argmax(Q[state[0], state[1], :])

	return action
