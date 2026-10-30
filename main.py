import numpy as np
import matplotlib.pyplot as plt
from src.ga_framework import population
from src.fitness_sim import fitness_sim


pop = population(10, 3, fitness_sim)

fig, axes = plt.subplots(5, 2, figsize=(8, 10))

target = 10
time = 10
step = 0.1
mass = 0.5

for i in range(5):
	a = pop.chroms[i][0] * target + target / pop.chroms[i][1]
	error = target
	sum_errors = error
	v = 0
	t = np.linspace(0, time, int(time / step))
	x = [0]
	for j in range(1, len(t)):
		x.append(v * step + x[j - 1])
		last_error = error
		error = target - x[j]
		sum_errors += error
		a = (pop.chroms[i][0] * error + sum_errors / pop.chroms[i][1] + (error - last_error) * pop.chroms[i][2]) / mass
		v += a * step
		
	axes[i][0].plot(t, x)
	
pop.evolution(5000, 0.2)

for i in range(5):
	a = pop.chroms[i][0] * target + target / pop.chroms[i][1]
	error = target
	sum_errors = error
	v = 0
	t = np.linspace(0, time, int(time / step))
	x = [0]
	for j in range(1, len(t)):
		x.append(v * step + x[j - 1])
		last_error = error
		error = target - x[j]
		sum_errors += error
		a = (pop.chroms[i][0] * error + sum_errors / pop.chroms[i][1] + (error - last_error) * pop.chroms[i][2]) / mass
		v += a * step
		
	axes[i][1].plot(t, x)
		
axes[0][0].set_title('First Generation')
axes[0][1].set_title('Last Generation')
plt.show()
