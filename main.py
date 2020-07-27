import math
import numpy as np
import matplotlib.pyplot as plt

#triangulo1 = [[25.774252, -80.190262],
#        [18.466465, -66.118292],
#        [32.321384, -64.75737],
#        [25.774252, -80.190262]]

triangulo1 = [[2, 1], [4,2], [3,4], [2,1]]

x1 = [point[0] for point in triangulo1]
y1 = [point[1] for point in triangulo1]

giro1 = np.matrix([[math.sqrt(3)/2, -1/2], [1/2, math.sqrt(3)/2]]);
giro2 = np.matrix([[math.sqrt(2)/2, math.sqrt(2)/2], [-math.sqrt(2)/2, math.sqrt(2)/2]]);


plt.plot(x1,y1, 'b')
plt.plot(x1,y1, 'bo')

print (triangulo1)
print (np.transpose(triangulo1))

triangulo2 = np.array(np.transpose(giro1 * np.transpose(triangulo1)));

print (triangulo2)

x2 = [point[0] for point in triangulo2]
y2 = [point[1] for point in triangulo2]

plt.plot(x2,y2, 'r')
plt.plot(x2,y2, 'ro')

triangulo3 = np.array(np.transpose(giro2 * np.transpose(triangulo2)));

x3 = [point[0] for point in triangulo3]
y3 = [point[1] for point in triangulo3]

plt.plot(x3,y3, 'g')
plt.plot(x3,y3, 'go')

plt.axis([0, 6, 0, 6])
plt.show()