import matplotlib.pyplot as plt

line_1 = []
line_2 = []

file = open('RL_EXP_OUT.dat')
for line in file:
	(point_1, point_2) = line.split()
	line_1.append(point_1)
	line_2.append(point_2)

x_axis = [i for i in range(1, len(line_1)+1)]


plt.plot(x_axis, line_1, 'r')
plt.plot(x_axis, line_2, 'b')
plt.xlabel('Steps')
plt.ylabel('% Optimal action')
plt.savefig('figure_2_3.pdf')
