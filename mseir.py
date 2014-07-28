import numpy as np
import matplotlib.pyplot as plt
import seaborn



N = 2400000.
mu = 1./21900.
births = 138.
r0 = 17.2
gamma = 1./14. # recovery rate

L = 156500
dt = 0.2
T = np.linspace(0, L/365., L/dt)

S = np.arange(0, L, dt)
I = np.arange(0, L, dt)
R = np.arange(0, L, dt)

S[0] = 168000.
I[0] = 8.
R[0] = N - S[0] - I[0]



for t in range(1, len(S)) :

	S[t] = S[t-1] + dt * (births - r0 * (1. + np.sin(2*np.pi*t*dt/365.)/10.) * gamma * S[t-1] * I[t-1] / N - mu * S[t-1])
	I[t] = I[t-1] + dt * (r0 * (1. + np.sin(2*np.pi*t*dt/365.)/10.) * gamma * S[t-1] * I[t-1] / N - gamma * I[t-1] - mu * I[t-1])
	#R[t] = R[t-1] + dt * (gamma * I[t-1] - mu * R[t-1])
	

R = N - S - I


plt.plot(T, I)
plt.show()










"""
N = 2400000 # population
births = 137 # births per day
delta = 1./120 # maternal immunity waning rate
mu = 1./21900 # death rate
r0 = 18.
sigma = 1./6 # rate of becoming symptomatic
gamma = 1./14 # recovery rate

L = 7300
dt = 0.05
T = np.linspace(0, L/365., L/dt)

M = np.arange(0, L, dt)
S = np.arange(0, L, dt)
E = np.arange(0, L, dt)
I = np.arange(0, L, dt)
R = np.arange(0, L, dt)

M[0] = 0.005 * N
S[0] = 0.05 * N
E[0] = 0.0005 * N
I[0] = 0.0005 * N
R[0] = N - S[0] - E[0] - I[0] - R[0]



for t in range(1, len(S)) :
	#M[t] = M[t-1] + dt * (births - delta * M[t-1] - mu * M[t-1])
	#S[t] = S[t-1] + dt * (delta * M[t-1] - r0 * gamma * S[t-1] * I[t-1] / N - mu * S[t-1])
	#E[t] = E[t-1] + dt * (r0 * gamma * S[t-1] * I[t-1] / N - mu * E[t-1] - sigma * E[t-1])
	#I[t] = I[t-1] + dt * (sigma * E[t-1] - mu * I[t-1] - gamma * I[t-1])
	
	S[t] = S[t-1] + dt * (births - (1+np.sin(2*np.pi*T[t])/10) * r0 * gamma * S[t-1] * I[t-1] / N - mu * S[t-1])
	I[t] = I[t-1] + dt * ((1+np.sin(2*np.pi*T[t])/10) * r0 * gamma * S[t-1] * I[t-1] / N - mu * I[t-1] - gamma * I[t-1])


#R = N - M - S - E - I
R = N - S - I


plt.plot(T, I)
plt.show()
"""