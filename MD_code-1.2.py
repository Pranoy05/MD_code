# written from scratch
# ver 1.2
# + code to calculate total KE, PE and TE at each frame

import math
import random
import matplotlib.pyplot as plt
import pandas as pd

# --initialisation--

# 1) system set up
N = 100 # no. of particles
init_pos = [random.uniform(-1.5, 1.5) for i in range(N)] # initial positions
init_vel = [random.uniform(-1.5, 1.5) for i in range(N)] # initial velocities
masses = [1.0 for i in range(N)] # masses of each of the particles

# 2) defining forcefield 
Uo = 20.0

# function to calculate force
# F = -dU/dx ; U = Uo[(1-x^2)^2]
def calc_force(x):
    return 4* Uo* x* (1-x**2)

# 3) simlulation parameters
n_steps = 1000
dt = 0.01 # time step

# --simulation--
time = 0.0
positions = init_pos
velocities = init_vel

# lists to save trajectory data
all_times = []
all_positions = []
all_velocities = []
all_KE = []
all_PE = []
all_TE = []

# main loop: integrator (3 step velocity verlet)
for step in range(n_steps):
    
    # calculating forces at the beginning of the loop
    forces = [calc_force(positions[i]) for i in range(N)] 
    
    # calculating velocities at dt/2 according to these forces
    velocities = [velocities[i] + 0.5*dt *forces[i]/masses[i] for i in range(N)]  

    # calculating positions at dt
    positions = [positions[i] + dt*velocities[i] for i in range(N)] 

    # recaclculating forces for new positions (dt)
    forces = [calc_force(positions[i]) for i in range(N)]

    # calculating velocities at dt according to the new forces
    velocities = [velocities[i] + 0.5*dt*forces[i]/masses[i] for i in range(N)]

    # calculating PE, KE, and TE
    KE = sum((0.5 * masses[i] * (velocities[i])**2) for i in range(N))
    PE = sum(Uo * (1 - positions[i]**2)**2 for i in range(N))
    TE = KE + PE
    
    time += dt

    # saving the positions and velocities 
    all_times.append(time)
    all_positions.append(positions)
    all_velocities.append(velocities)
    all_PE.append(PE)
    all_KE.append(KE)
    all_TE.append(TE)

    if step%(n_steps/10) == 0: # terminal output once every 100 steps
        print(f"Step: {step}, Time: {time:.2f}")

print("Simulation finished.")

# --data storage--
data = {'time': all_times}

for i in range(N):
    data[f'particle_{i}_x'] = [x[i] for x in all_positions]
    data[f'particle_{i}_v'] = [v[i] for v in all_velocities]

# Create a df
df = pd.DataFrame(data)
df['PE'] = all_PE
df['KE'] = all_KE
df['TE'] = all_TE

# output CSV
df.to_csv('md_out.csv', index=False)
print(f'Output CSV file: md_out.csv')