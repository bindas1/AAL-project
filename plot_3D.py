import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def plot_cuboid(center, size, bin_, fig, ax):
    """
       Create a data array for cuboid plotting.


       ============= ================================================
       Argument      Description
       ============= ================================================
       center        center of the cuboid, triple
       size          size of the cuboid, triple, (x_length,y_width,z_height)
       :type size: tuple, numpy.array, list
       :param size: size of the cuboid, triple, (x_length,y_width,z_height)
       :type center: tuple, numpy.array, list
       :param center: center of the cuboid, triple, (x,y,z)
   """
    # suppose axis direction: x: to left; y: to inside; z: to upper
    # get the (left, outside, bottom) point

    ox, oy, oz = center
    l, w, h = size

    x = np.linspace(ox - l / 2, ox + l / 2, num=10)
    y = np.linspace(oy - w / 2, oy + w / 2, num=10)
    z = np.linspace(oz - h / 2, oz + h / 2, num=10)
    x1, z1 = np.meshgrid(x, z)
    y11 = np.ones_like(x1) * (oy - w / 2)
    y12 = np.ones_like(x1) * (oy + w / 2)
    x2, y2 = np.meshgrid(x, y)
    z21 = np.ones_like(x2) * (oz - h / 2)
    z22 = np.ones_like(x2) * (oz + h / 2)
    y3, z3 = np.meshgrid(y, z)
    x31 = np.ones_like(y3) * (ox - l / 2)
    x32 = np.ones_like(y3) * (ox + l / 2)

    c = np.random.rand(3)

    # outside surface
    ax.plot_wireframe(x1, y11, z1, color=c, rstride=1, cstride=1, alpha=0.6)
    # inside surface
    ax.plot_wireframe(x1, y12, z1, color=c, rstride=1, cstride=1, alpha=0.6)
    # bottom surface
    ax.plot_wireframe(x2, y2, z21, color=c, rstride=1, cstride=1, alpha=0.6)
    # upper surface
    ax.plot_wireframe(x2, y2, z22, color=c, rstride=1, cstride=1, alpha=0.6)
    # left surface
    ax.plot_wireframe(x31, y3, z3, color=c, rstride=1, cstride=1, alpha=0.6)
    # right surface
    ax.plot_wireframe(x32, y3, z3, color=c, rstride=1, cstride=1, alpha=0.6)
    ax.set_xlabel('X')
    ax.set_xlim(0, bin_[0])
    ax.set_ylabel('Y')
    ax.set_ylim(0, bin_[1])
    ax.set_zlabel('Z')
    ax.set_zlim(0, bin_[2])

    return ax

boxes = []
with open("sample_generate.txt") as f:
    for line in f.readlines():
        edges = line.strip().split(',')
        edges = [float(edge) for edge in edges]
        boxes.append(edges)
bin_ = [500, 500, 0]

bin_copy = bin_.copy()
a_copy = boxes.copy()

for box in a_copy:
    h = bin_copy[2]
    bin_copy[2] += min(box)
    box.append(h)

fig = plt.figure()
ax = fig.gca(projection='3d')

for i in boxes:
    plot_cuboid((i[0]/2,i[1]/2,i[2]/2 + i[3]), (i[0],i[1],i[2]), bin_copy, fig, ax)
plt.show()
