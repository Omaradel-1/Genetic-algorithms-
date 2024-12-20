import random

# Fitness function: maximize f(x) = x^2
def fitness_function(x):
    return x ** 2

# Generate an initial population of random integers
def generate_population(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# Selection: choose the best individuals based on fitness
def select_parents(population, fitnesses):
    sorted_population = [x for _, x in sorted(zip(fitnesses, population), reverse=True)]
    return sorted_population[:2]  # Select top 2 individuals

# Crossover: combine two parents to create offspring
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(bin(parent1)) - 2)  # Binary crossover
    mask = (1 << crossover_point) - 1
    child1 = (parent1 & mask) | (parent2 & ~mask)
    child2 = (parent2 & mask) | (parent1 & ~mask)
    return child1, child2

# Mutation: introduce random changes
def mutate(individual, mutation_rate, lower_bound, upper_bound):
    if random.random() < mutation_rate:
        return random.randint(lower_bound, upper_bound)
    return individual

# Genetic algorithm main loop
def genetic_algorithm(pop_size, generations, lower_bound, upper_bound, mutation_rate):
    population = generate_population(pop_size, lower_bound, upper_bound)

    for generation in range(generations):
        fitnesses = [fitness_function(ind) for ind in population]
        parent1, parent2 = select_parents(population, fitnesses)

        # Generate offspring
        offspring = []
        for _ in range(pop_size // 2):
            child1, child2 = crossover(parent1, parent2)
            offspring.append(mutate(child1, mutation_rate, lower_bound, upper_bound))
            offspring.append(mutate(child2, mutation_rate, lower_bound, upper_bound))

        population = offspring  # Replace old population with offspring

        # Output best solution in the current generation
        best_individual = max(population, key=fitness_function)
        print(f"Generation {generation + 1}: Best = {best_individual}, Fitness = {fitness_function(best_individual)}")

    return max(population, key=fitness_function)

# Parameters
POPULATION_SIZE = 10
GENERATIONS = 20
LOWER_BOUND = 0
UPPER_BOUND = 100
MUTATION_RATE = 0.1

# Run the genetic algorithm
best_solution = genetic_algorithm(POPULATION_SIZE, GENERATIONS, LOWER_BOUND, UPPER_BOUND, MUTATION_RATE)
print(f"\nBest solution found: {best_solution} with Fitness = {fitness_function(best_solution)}")