import numpy as np

def fitness_sim(chroms, weight):
	target = 10
	sim_time = 10
	time_step = 0.1
	mass = 0.5
	
	chroms = chroms.tolist()
	fitnesses = np.zeros(len(chroms))
	for i in range(len(chroms)):
		acc = chroms[i][0] * target + target / chroms[i][1]
		vel = acc
		x1 = 0
		max_x = x1
		error = target
		sum_errors = error
		settling_time = sim_time
		overshoot = 0
		settling_counter = 0
		for j in range(1, int(sim_time / time_step)):
			x2 = vel * time_step + x1
			last_error = error
			error = abs(target - x2)
			sum_errors += error
			acc = (chroms[i][0] * error + sum_errors / chroms[i][1] + (error - last_error) * chroms[i][2]) / mass
			vel += acc * time_step
			
			if abs(x2 - x1) < 0.05:
				settling_counter += 1
				
			elif settling_counter < 30:
				settling_counter = 0
				
			if settling_counter == 30:
				settling_time = j * time_step
				
			x1 = x2
			max_x = max(max_x, x2)
			
		if max_x > target:
			overshoot = max_x
			
		if overshoot + settling_time + error != 0:
			fitnesses[i] = 1 / (overshoot + settling_time + error)
			
		else:
			fitnesses[i] = 1000
			
		
	return fitnesses

