from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


def get_test_data(delta=0.05):

    from matplotlib.mlab import bivariate_normal
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)

    Z1 = bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    Z2 = bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
    Z = Z2 - Z1

    X = X * 10
    Y = Y * 10
    Z = Z * 500
    return X, Y, Z


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y, z = axes3d.get_test_data(0.05)

ax.plot_wireframe(x,y,z, rstride=5, cstride=5)

plt.show()


