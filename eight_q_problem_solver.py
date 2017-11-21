from genetic_algo import GA
import random
class eqp_solver:

	def random_generator(self):
		child = ''
		for i in range(8):
			child += str(random.randrange(1,9))
		return child

	def fitness_function(self,individual):
		attacking = 0
		for i in range(8):
			for j in range(i+1,8):
				if individual[i] == individual[j]:
					attacking += 1
		for i in range(8):
			for j in range(i+1,8):
				if j-i == abs(int(individual[j]) - int(individual[i])):
					attacking += 1

		return 8-attacking

	def reproduce(self,parent1,parent2):
		index = random.randrange(1,8)
		child = parent1[0:index]
		child += parent2[index:]
		return child

	def success_check(self,population,fitness):
		for i in range(len(population)):
			if fitness[i] == 8:
				print(population[i])
				return True
		return False

	def mutation_function(self,individual):
		index = random.randrange(0,8)
		individual = individual[0:index] + str(random.randrange(1,9)) + individual[index+1:]
		return individual

eqp = eqp_solver()

options = {
	'max_population' : 100,
	'death_rate' : 0.3,
	'mutation_rate' : 0.2,
	'reproduction_type' : 'sexual',
	'random_generator' : eqp.random_generator,
	'fitness_function' : eqp.fitness_function,
	'reproduction_function' : eqp.reproduce,
	'mutation_function' : eqp.mutation_function
}

ga = GA(options)

best_individual,best_fitness = ga.evolve(10000000,eqp.success_check)

print("\nBest ---")
print(best_individual)
print(best_fitness)