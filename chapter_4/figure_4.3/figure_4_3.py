import numpy as np

# global variables
# win_prob = 0.25
# win_prob = 0.55
win_prob = 0.4
gamma = 1

def initialize():
	array_state_value = np.zeros(101) # with two dummy state 0 and 100
	# array_state_value[100] = 0

	return array_state_value

def optimal_value_choose(state, array_state_value):
	upper_bound = min(state, 100-state)
	lower_bound = 0

	action_list = list(range(0, upper_bound+1))

	maximum_value = 0.0
	optimal_action = 101
	for action in action_list:
		s_next_loss = state - action
		s_next_win = state + action

		# define the reward
		reward_loss = 0
		reward_win = 0
		if s_next_win == 100:
			reward_win = 1

		value = (win_prob*(reward_win+(gamma*array_state_value[s_next_win]))) + ((1-win_prob)*(reward_loss+gamma*(array_state_value[s_next_loss])))
		# value = (win_prob*array_state_value[s_next_win]) + ((1-win_prob)*array_state_value[s_next_loss])
		if value >= maximum_value:
			maximum_value = value
			optimal_action = action
		

	return (maximum_value, optimal_action)

def save_result_estimate(array_state_value, sweep_time):
	tem = np.delete(array_state_value, 0)
	array_state_value = np.delete(tem, len(tem)-1)

	file_name = "estimate_sweep_" + str(sweep_time) + ".dat"

	# save result (for value estimate)
	with open(file_name, "w") as data_file:
		for i in range(len(array_state_value)):
			data_file.write("{0}\n".format(array_state_value[i]))

def save_result_final_policy(final_optimal):
	tem = np.delete(final_optimal, 0)
	final_optimal = np.delete(tem, len(tem)-1)

	# save result (for final policy)
	with open("final_out.dat", "w") as data_file:
		for i in range(len(final_optimal)):
			data_file.write("{0}\n".format(int(final_optimal[i])))

def value_iteration():
	array_state_value = initialize()
	# initialize the final optimal
	final_optimal = [0]*101
	sweep_time = 0

	theta = 1e-15
	while(True):
		delta = 0

		sweep_time += 1
		
		for state in range(1,100):
			tem_value = array_state_value[state]
			(array_state_value[state], final_optimal[state]) = optimal_value_choose(state, array_state_value)
			delta = max(delta, np.absolute(tem_value - array_state_value[state]))

		# if(sweep_time == 1 or sweep_time == 2 or sweep_time == 3 or sweep_time == 23):
		if(sweep_time == 1 or sweep_time == 2 or sweep_time == 3 or sweep_time == 27):
			save_result_estimate(array_state_value, sweep_time)

		if delta < theta:
			break

	print("Total sweep time is " + str(sweep_time))
	save_result_final_policy(final_optimal)
	

if __name__ == "__main__":
	value_iteration()