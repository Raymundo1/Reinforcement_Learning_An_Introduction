"""
	Author: Xinlei Chen
	windy_gridworld with king's move [4 actions]
"""
from utils import rand_norm, rand_in_range, rand_un
import numpy as np 

# num_total_states
last_state = None

# wind strength
wind_strength = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

# state information
start_state = np.array([3, 0])
goal_state = np.array([3, 7])

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

	# N -> North, S -> South, E -> East, W -> West
	tem = np.copy(last_state)
	if(action == 0):
		current_state = action_N(tem)
	elif(action == 1):
		current_state = action_E(tem)
	elif(action == 2):
		current_state = action_S(tem)
	elif(action == 3):
		current_state = action_W(tem)


	current_state[0] = current_state[0] - wind_strength[last_state[1]]
	if current_state[0] < 0:
		current_state[0] = 0

	reward = -1.0
	is_terminal = False

	# print((current_state == goal_state).all())
	if (current_state == goal_state).all():
		is_terminal = True
		current_state = None
		reward = 0.0


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
	Function for do action
"""
def action_N(state):
	state[0] = state[0] - 1

	if state[0] < 0:
		state[0] = 0

	return state

def action_E(state):
	state[1] = state[1] + 1

	if state[1] > 9:
		state[1] = 9

	return state


def action_S(state):
	state[0] = state[0] + 1

	if state[0] > 6:
		state[0] = 6

	return state


def action_W(state):
	state[1] = state[1] - 1

	if state[1] < 0:
		state[1] = 0

	return state
