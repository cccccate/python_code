# author: lccate
# time: 2018.11.26
# description: This is a simple python file to extract loss value from txt of Faster R-CNN training.


import matplotlib.pyplot as plt

input = open('1124.txt', 'r')

coordinate_y = []

for line in input:
    line = line.split()
    if 'total' in line:
        coordinate_y.append(float(line[-1]))

hostt = plt.subplot(111)
hostt.set_xlabel("iterations")
hostt.set_ylabel("RPN loss")

plt.plot(coordinate_y)
plt.grid(True)
plt.show()
