import random

class GA:

	def __init__(self, options):
		self.max_population = options['max_population']
		self.death_rate = options['death_rate']
		self.mutation_rate = options['mutation_rate']
		self.reproduction_type = options['reproduction_type']
		self.random_generator = options['random_generator']
		self.fitness_function = options['fitness_function']
		self.reproduction_function = options['reproduction_function']
		self.mutation_function = options['mutation_function']
		self.fitness = [-float('inf') for i in range(self.max_population)]
		self.population = []

	def initialize_random(self):
		for i in range(self.max_population):
			self.population.append(self.random_generator())

	def update_fitness(self):
		for i in range(self.max_population):
			self.fitness[i] = self.fitness_function(self.population[i])

	def sort_by_fitness(self):
		zipped = list(reversed(sorted(zip(self.fitness,self.population))))
		self.fitness = [x for x,y in zipped]
		self.population = [y for x,y in zipped]

	def eliminate(self):
		self.population = self.population[:int(self.max_population)-int(self.max_population*self.death_rate)]
		self.survived_size = len(self.population)

	def reproduce(self):
		if self.reproduction_type == 'sexual':
			random_parent_1 = self.population[random.randrange(0,self.survived_size)]
			random_parent_2 = self.population[random.randrange(0,self.survived_size)]
			return self.reproduction_function(random_parent_1,random_parent_2)
		else:
			#TODO
			random_parent_1 = random.randrange(0,self.survived_size)
			random_parent_2 = random.randrange(0,self.survived_size)
			return self.reproduce(random_parent_1,random_parent_2)

	def create_new_members(self):
		while len(self.population) < self.max_population:
			new_baby = self.reproduce()
			self.population.append(new_baby)

	def mutate(self):
		for i in range(len(self.population)):
			if random.random() < self.mutation_rate:
				self.population[i] = self.mutation_function(self.population[i])

	def iterate_once(self):
		self.update_fitness()
		self.sort_by_fitness()
		self.eliminate()
		self.create_new_members()
		self.mutate()

	def print_after_generation(self,i):
		print("\n")
		print("Generation "+str(i))
		print("Best Fitness : "+str(max(self.fitness)))
		print("Best Individual: "+str(self.population[0]))

	def evolve(self, max_generations, success_check):
		self.initialize_random()
		self.print_after_generation(0)

		for i in range(max_generations):
			self.iterate_once()
			self.print_after_generation(i+1)

			if success_check(self.population,self.fitness):
				break
		return self.population[0], self.fitness[0]








