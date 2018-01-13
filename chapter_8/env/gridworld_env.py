"""
	Author: Xinlei Chen
	GridWord environment
"""

import numpy as np 

last_state = None

# state information
start_state = np.array([2, 0])
goal_state = np.array([0, 8])

# obstacle
obstacle_state = [[1, 2], [2, 2], [3, 2], [0, 7], [1, 7], [2, 7], [4, 5]]


def env_init():
	global last_state

	last_state = np.array([0, 0])


def env_start():
	""" returns numpy array """
	global last_state

	last_state = start_state

	return last_state


def env_step(action):
	"""
	Arguments
	---------
	action : int
		the action taken by the agent in the current state

	Returns
	---------
	result : dict
		dictionary with keys {reward, state, isTerminal} containing the results
		of the action taken
	"""
	global last_state

	if action < 0 or action > 3:
		print "Invalid action take!!"
		print "action : ", action
		print "current_state : ", last_state
		exit(1)

	tem = np.copy(last_state)
	if(action == 0):
		current_state = action_up(tem)
	elif(action == 1):
		current_state = action_right(tem)
	elif(action == 2):
		current_state = action_down(tem)
	else:
		current_state = action_left(tem)

	reward = 0.0
	is_terminal = False

	if (current_state == goal_state).all():
		is_terminal = True
		current_state = None
		reward = 1.0

	last_state = current_state
	result = {"reward": reward, "state": current_state, "isTerminal": is_terminal}

	return result

def env_cleanup():
	"""
		This function is not used
	"""
	return

def env_message(in_message):
	"""
	Arguments
	---------
	inMessage : string
		the message being passed

	Returns
	-------
	string : the response to the message
	"""
	return ""

"""
	Consequence of the specific action
"""
def action_up(state):
	state[0] = state[0] - 1

	if list(state) in obstacle_state:
		state[0] = state[0] + 1

	if state[0] < 0:
		state[0] = 0

	return state

def action_right(state):
	state[1] = state[1] + 1

	if list(state) in obstacle_state:
		state[1] = state[1] - 1

	if state[1] > 8:
		state[1] = 8

	return state

def action_down(state):
	state[0] = state[0] + 1

	if list(state) in obstacle_state:
		state[0] = state[0] - 1

	if state[0] > 5:
		state[0] = 5

	return state

def action_left(state):
	state[1] = state[1] - 1

	if list(state) in obstacle_state:
		state[1] = state[1] + 1

	if state[1] < 0:
		state[1] = 0

	return state



