"""
	Author: Xinlei Chen
	one-step Sarsa agent Algorithm [4 actions] 
"""

from utils import rand_norm, rand_in_range, rand_un
import numpy as np

num_actions = 4
last_action = None
last_state = None

# basic Sarsa arugment
epsilon = 0.1
alpha = 0.5

Q = None

def agent_init():
	"""
	Returns: nothing
	"""
	global last_action, last_state, Q
	last_action = 0
	last_state = np.array([0, 0])

	Q = np.zeros((7, 10, num_actions))


def agent_start(state):
	"""
	Arguments: states: numpy array
	Returns: action: integer
	"""
	global last_action, last_state

	# 0 represent exploration, 1 represent exploitation
	choice = np.array([0,1])
	result = np.random.choice(choice, p=[epsilon, 1-epsilon])

	if result == 0:
		# exploration
		action = rand_in_range(num_actions)
 
	else:
		# exploitation
		action = np.argmax(Q[state[0], state[1], :])

	last_action = action
	last_state = state

	return action


def agent_step(reward, state):
	"""
	Arguments: reward: floating point, state: integer
	Returns: action: integer
	"""
	global Q, last_action, last_state

	# choose A' from S' using policy derived from Q
	# 0 represent exploration, 1 represent exploitation
	choice = np.array([0,1])
	result = np.random.choice(choice, p=[epsilon, 1-epsilon])

	if result == 0:
		# exploration
		action = rand_in_range(num_actions)
 
	else:
		# exploitation
		action = np.argmax(Q[state[0], state[1], :])

	Q[last_state[0], last_state[1], last_action] = Q[last_state[0], last_state[1], last_action] + \
		 alpha*(reward + Q[state[0], state[1], action] -  Q[last_state[0], last_state[1], last_action])

	last_state = state
	last_action = action

	return action


def agent_end(reward):
	"""
	Arguments: reward: floating point
	Returns: Nothing
	"""
	pass


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
	global alpha, epsilon

	piece = in_message.split()

	if(piece[1] == "alpha"):
		alpha = float(piece[3])
		print "successfully set alpha to ", alpha

	elif(piece[1] == "epsilon"):
		epsilon = float(piece[3])
		print "successfully set epsilon to ", epsilon
	
	# else
	return "I don't know how to respond to your message"

