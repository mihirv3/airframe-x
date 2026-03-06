import numpy as np
import matplotlib.pyplot as plt

m = 0.2
L = 0.3
g = 9.81
b = 0.05
I = m * L ** 2
dt = 0.02
t_end = 10
PWM = 1500
Ct = 0.003
F = (PWM - 1000) * Ct
tau_thrust = F * L

theta = -90
theta_dot = 0
theta_ddot = 0

n_times = int(t_end/dt)

t_vals = []
theta_vals = []


for i in range(n_times):
    t = i * dt
    theta_ddot = (tau_thrust - m * g * L * np.cos(theta) - b * theta_dot)/I
    theta_dot += theta_ddot*dt
    theta += theta_dot*dt

    t_vals.append(t)
    theta_vals.append(theta)
m = 0.2
L = 0.3
g = 9.81
b = 0.05
I = m * L ** 2
dt = 0.02
t_end = 10
PWM = 1500
Ct = 0.003
F = (PWM - 1000) * Ct
tau_thrust = F * L

theta = -90
theta_dot = 0
theta_ddot = 0

n_times = int(t_end/dt)

t_vals = []
PWM_vals = []


for i in range(n_times):
    t = i * dt

    if t < 2:
        PWM = 900
    else:
        PWM = 1500

    theta_ddot = (tau_thrust - m * g * L * np.cos(theta) - b * theta_dot)/I
    theta_dot += theta_ddot*dt
    theta += theta_dot*dt

    t_vals.append(t)
    PWM_vals.append(PWM)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

ax1.plot(t_vals, theta_vals)
ax2.plot(t_vals, PWM_vals)
plt.show()
