# MD_code
A simple molecular dynamics (MD) simulation code written from the ground up. Part of my internship at IITK.

Initial version: 
written by Gemini AI. Used to get an outline.  

Ver. 1.0: 
Forcefield is a 1D double well potential, U(x) = Uo (1-x^2)^2 
Integrator is a 3-step Velocity Verlet. 
Has a feature to plot final position and position vs time for the simulated particles.

Ver. 1.1: 
Better plots: 
1. Histogram of inital and final positions
2. Position vs time plot
3. Velocity vs time plot

Ver. 1.2: 
Final(?) version for 1D
Calculation of PE, KE, and TE. 
Plotting function removed. 
Output now given as a CSV file with each position and velocity, along with time, KE, PE, TE. 

Ver. 1.2 is uploaded as a .py file, rest are available in a .ipynb file (MD_code-1.2.ipynb).
