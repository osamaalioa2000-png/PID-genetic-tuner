import numpy as np

rng = np.random.default_rng(42)
class population():
	def __init__(self, pop_size, gene_num, fit_func):
		self.pop_size = pop_size
		self.gene_num = gene_num
		
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
		
	def select(self, select_type, sample_size=1):
		if select_type == 'wheel':
			return rng.choice(self.fitnesses, size=(2, (self.pop_size + 1) // 2), weights=self.fitnesses, k=1)
			
		elif select_type == 'tournament':
			contenders = np.random.choice(self.pop_size, size=(self.pop_size, sample_size))
			winners_ind = contenders[self.rang, np.argmax(self.fitnesses[contenders], axis=1)]
			winners = self.chroms[winners_ind]
			return winners
			
		
	def crossover(self, parents):
		new_gen = np.zeros((self.pop_size + (self.pop_size % 2), self.gene_num))
		i = 0
		for parent1i in range(int(self.pop_size / 2) + (self.pop_size % 2)):
			parent2 = parents[np.random.choice(self.pop_size)]
			attempts = 0
			while np.all(parent1i == parent2) and attempts <= self.pop_size:
				parent2 = parents[np.random.choice(self.pop_size)]
				attempts += 1
				
			alpha = rng.random(self.gene_num)
			child1 = alpha * np.abs(parents[parent1i] - parent2) + np.min([parents[parent1i], parent2], axis=0)
			new_gen[i] = child1
			i += 1
			child2 = (1 - alpha) * np.abs(parents[parent1i] - parent2) + np.min([parents[parent1i], parent2], axis=0)
			new_gen[i] = child2
			i += 1
			
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
			parents = self.select('tournament', self.sample_size)
			children = self.crossover(parents)
			self.chroms = self.mutate(children, mutation_rate)
			
			self.fitnesses = self.fit_func(self.chroms, self.average_fitness / self.max_fitness)
			self.average_fitness = sum(self.fitnesses) / self.pop_size
			self.max_fitness = max(self.fitnesses)
			
		
	
