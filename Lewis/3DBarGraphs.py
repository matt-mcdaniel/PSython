from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
axl = fig.add_subplot(111, projection = '3d')

xpos = [1,2,3,4,5,6,7,8,9,10]
ypos = [2,3,4,5,1,6,2,1,7,2]
zpos = [0,0,0,0,0,0,0,0,0,0]

dx = np.ones(10)
dy = np.ones(10)
dz = [1,2,3,4,5,6,7,8,9,10]

axl.bar3d(xpos, ypos, zpos, dx, dy, dz, color = '#00ceaa')
plt.show()
