'''
	Author: Xinlei Chen
	
'''

import matplotlib.pyplot as plt 

sweep_1 = []
sweep_2 = []
sweep_3 = []
sweep_final = []

sweep_order = [1, 2, 3, 27]
for i in sweep_order:
	file_name = "estimate_sweep_" + str(i) + ".dat"
	file = open(file_name)

	for line in file:
		point = line

		if i == 1:
			sweep_1.append(point)

		elif i == 2:
			sweep_2.append(point)

		elif i == 3:
			sweep_3.append(point)

		else:
			sweep_final.append(point)

	file.close()

x_axis = [i for i in range(1, len(sweep_final)+1)]

plt.plot(x_axis, sweep_1, color='r', label='sweep 1')
plt.plot(x_axis, sweep_2, color='b', label='sweep 2')
plt.plot(x_axis, sweep_3, color='g', label='sweep 3')
plt.plot(x_axis, sweep_final, color='k', label='sweep 27')
# plt.plot(x_axis, sweep_final, color='k', label='sweep 23')
plt.legend(bbox_to_anchor=(1.0, 0.01), loc=4, borderaxespad=0.)

plt.xlabel('Capital')
plt.ylabel('Value estimates')
# plt.show()

plt.savefig('estimate_40.pdf')
