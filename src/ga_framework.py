import numpy as np

rng = np.random.default_rng(42)
class population():
	def __init__(self, pop_size, gene_num, fit_func, select_type):
		"""
		A modular genetic algorithm framework
		Parameters:
        -----------
        pop_size : int
            The number of candidate solutions in each generation.
		gene_num : int
			The number of genese for every chromosome.
        fit_func : callable
            A custom function that takes in chromosomes and returns their fitness scores.
		select_type : string
			The selection type used in the select method (wheel, tournament)
		"""
		
		self.pop_size = pop_size
		self.gene_num = gene_num
		
		self.select_type = select_type
		self.gene_init_scale = [1, 10 ** 9, 10]
		self.chroms = np.zeros((self.gene_num, self.pop_size))
		for i in range(gene_num):
			self.chroms[i] = np.random.random(pop_size) * self.gene_init_scale[i]
			
		self.chroms = self.chroms.T
		
		self.fit_func = fit_func
		self.fitnesses = self.fit_func(self.chroms, 1)
		self.average_fitness = sum(self.fitnesses) / self.pop_size
		self.max_fitness = max(self.fitnesses)
		
		self.sample_size = 4
		self.mutation_scale = 1
		
	def select(self):
		if self.select_type == 'wheel':
			ind = np.random.choice(self.rang, size=(self.pop_size), p=(self.fitnesses / np.sum(self.fitnesses)))
			return self.chroms[ind]
			
		elif self.select_type == 'tournament':
			contenders = np.random.choice(self.pop_size, size=(self.pop_size, self.sample_size))
			winners_ind = contenders[self.rang, np.argmax(self.fitnesses[contenders], axis=1)]
			winners = self.chroms[winners_ind]
			return winners
			
		
	def crossover(self, parents):
		new_gen = np.zeros((self.pop_size + (self.pop_size % 2), self.gene_num))
		for i in range(int(self.pop_size / 2) + (self.pop_size % 2)):
			parent2 = parents[np.random.choice(self.pop_size)]
			attempts = 0
			while np.all(i == parent2) and attempts <= self.pop_size:
				parent2 = parents[np.random.choice(self.pop_size)]
				attempts += 1
				
			alpha = rng.random(self.gene_num)
			child1 = alpha * np.abs(parents[i] - parent2) + np.min([parents[i], parent2], axis=0)
			new_gen[i * 2] = child1
			child2 = (1 - alpha) * np.abs(parents[i] - parent2) + np.min([parents[i], parent2], axis=0)
			new_gen[i * 2 + 1] = child2
			
		if self.pop_size % 2 != 0:
			new_gen = new_gen[:-1]
			
		return new_gen
		
	def mutate(self, chroms, mutation_rate):
		mutation_mask = rng.random(chroms.shape) < mutation_rate
		mutants = chroms + rng.random(chroms.shape) * self.mutation_scale * mutation_mask
		return mutants
		
	def evolution(self, number_of_generations, mutation_rate):
		self.rang = np.arange(self.pop_size)
		for _ in range(number_of_generations):
			parents = self.select()
			children = self.crossover(parents)
			self.chroms = self.mutate(children, mutation_rate)
			
			self.fitnesses = self.fit_func(self.chroms, self.average_fitness / self.max_fitness)
			self.average_fitness = sum(self.fitnesses) / self.pop_size
			self.max_fitness = max(self.fitnesses)
			
		
	
