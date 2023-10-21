from vpython import *

# Function to create a 3D grid
def make_grid_3d(xmax, dx, c):
    for x in range(-xmax, xmax + dx, dx):
        curve(pos=[vector(x, xmax, 0), vector(x, -xmax, 0)], color=color.yellow, canvas=c)
    for y in range(-xmax, xmax + dx, dx):
        curve(pos=[vector(xmax, y, 0), vector(-xmax, y, 0)], color=color.magenta, canvas=c)

# Function to create 3D axes
def make_axes(length, c):
    xaxis = arrow(canvas=c, pos=vector(-90000, 90000, 0), axis=length * vector(1, 0, 0), color=color.red)
    yaxis = arrow(canvas=c, pos=vector(-90000, 90000, 0), axis=length * vector(0, 1, 0), color=color.green)
    zaxis = arrow(canvas=c, pos=vector(-90000, 90000, 0), axis=length * vector(0, 0, 1), color=color.blue)
    fudge = 0.06 * length
    xlabel = label(text="X", color=color.white, pos=xaxis.pos + xaxis.axis + vector(0, fudge, 0), box=False)
    ylabel = label(text="Y", color=yaxis.color, pos=yaxis.pos + yaxis.axis + vector(0, fudge, 0), box=False)
    zlabel = label(text="Z", color=zaxis.color, pos=zaxis.pos + zaxis.axis + vector(0, fudge, 0), box=False)

# User input for parameters
xmax = int(input("Enter the value for xmax: "))
dx = int(input("Enter the value for dx: "))
length = int(input("Enter the length for axes: "))

# Create a canvas
c1 = canvas(background=color.black, width=800, height=800)

# Create axes and grid
make_axes(length, c1)
make_grid_3d(xmax, dx, c1)

# User input for cylinder parameters
l_shaft = int(input("Enter the length of the shaft: "))
r_shaft = int(input("Enter the radius of the shaft: "))
l_manipulator = int(input("Enter the length of the manipulator: "))
r_manipulator = int(input("Enter the radius of the manipulator: "))

# Create cylinders
b1 = cylinder(canvas=c1, pos=vector(0, 0, 0), axis=vector(-l_shaft, -l_shaft/2, 0), radius=r_shaft, color=color.red)
b2 = cylinder(canvas=c1, pos=b1.axis, axis=vector(-l_manipulator, 0, 0), radius=r_manipulator, color=color.green)

f = 25

for i in range(1110):
    rate(4)
    b1.pos.x += 100 * X[i]
    b1.pos.y += 100 * Y[i]
    b1.pos.z += 2 * Z[i]
    b1.axis = Rx((1/f**2) * radians(Roll[i]), b1.axis)
    b1.axis = Ry((1/f**2) * radians(Pitch[i]), b1.axis)
    b1.axis = Rz((1/f**2) * radians(Yaw[i]), b1.axis)
    b2.pos.x = b1.pos.x + b1.axis.x
    b2.pos.y = b1.pos.y + b1.axis.y
    b2.pos.z = b1.pos.z + b1.axis.z
    b2.axis = Rx(radians((4/f) * Roll_o[i]), b2.axis)
    b2.axis = Ry(radians((4/f) * Pitch_o[i]), b2.axis)
    b2.axis = Rz(radians((4/f) * Yaw_o[i]), b2.axis)
