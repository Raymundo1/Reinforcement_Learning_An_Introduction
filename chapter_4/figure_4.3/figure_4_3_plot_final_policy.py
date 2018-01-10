import matplotlib.pyplot as plt

point_total = []

file = open('final_out.dat')
for line in file:
	point = line
	point_total.append(point)

file.close()

print(len(point_total))
x_axis = [i for i in range(1, len(point_total)+1)]


plt.bar(x_axis, point_total, fc='b')
plt.xlabel('Capital')
plt.ylabel('Final policy(stack)')
# plt.show()
plt.savefig('final_policy_40.pdf')
