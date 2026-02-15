# ==========================================
# PHYSICS ENGINE: Gravity & Integration
# ==========================================
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

N = 100 # number of stars
G = 1 # Gravitational constant
DT = 0.001



plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 8))
sizes = np.random.uniform(2, 20, N)

pos = np.random.randn(N, 2) * 1.5 #random positions for N stars

mass = np.random.uniform(1, 10, size=(N, 1))  # Random masses between 1-10 for N stars

acc = np.zeros((N, 2)) # initiate empty place holder for acceleration
vel = np.random.randn(N, 2) * 0.01

while True:
    # Calculate acceleration for all stars
    acc = np.zeros((N, 2))
    for i in range(N): # i: target star
        a_x = 0 
        a_y = 0
        for j in range(N): # j: non target star
            if j!=i:

                r_x = pos[j, 0] - pos [i, 0]
                r_y = pos[j, 1] - pos[i, 1]
                r = np.sqrt(r_x**2 + r_y**2 + 0.1) # softening factor to prevent infinite gravity at r=0

                a_x_i = (G * mass[j, 0] / r**3) * r_x
                a_y_j = (G * mass[j, 0] / r**3) * r_y

                a_x += a_x_i
                a_y += a_y_j

        acc[i] = (a_x, a_y)


    # Calculate velocity for all stars
    vel = vel + acc * DT

    # Calculate position for all stars
    pos = pos + vel * DT

    # and then figure out how to loop




    # Plotting
    ax.clear()
    ax.set_axis_off()          # Hides the white lines and numbers
    fig.patch.set_facecolor('black') # Makes the border of the window black
    ax.set_facecolor('black')  # Makes the plot area black

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    
    ax.scatter(pos[:, 0], pos[:, 1], color='#e0f7fa',  s=sizes, edgecolors='none')

    plt.pause(0.01) 