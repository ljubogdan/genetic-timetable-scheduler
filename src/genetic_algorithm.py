import crossover
import mutation
from chromosome import Chromosome
from constants import MUTATION_RANGE, POPULATION_SIZE, MAX_GENERATIONS
import matplotlib.pyplot as plt
import random

def genetic_algorithm(population):
    """
    Perform the genetic algorithm to evolve the population of chromosomes.
    The algorithm will run for a maximum number of generations or until a solution is found.

    Also, plot the fitness of the best 2 chromosomes in each generation.
    """

    if not isinstance(population, list) or not all(isinstance(chromosome, Chromosome) for chromosome in population):
        raise TypeError("Population must be a list of Chromosome instances.")

    if len(population) < POPULATION_SIZE:
        raise ValueError(f"Population size must be at least {POPULATION_SIZE}.")
    
    if not population:
        raise ValueError("Population cannot be empty.")
    
    best_fitness = []
    best_chromosomes = []

    # Calculate fitness for each chromosome in the initial population
    for chromosome in population:
        if not isinstance(chromosome, Chromosome):
            raise TypeError("Each member of the population must be an instance of the Chromosome class.")
        chromosome.calculate_fitness()

    for generation in range(MAX_GENERATIONS):
        # Sort the population by fitness in descending order
        population.sort(key=lambda x: x.fitness, reverse=True)

        # Store the best chromosomes for plotting
        best_fitness.append(population[0].fitness)
        best_chromosomes.append(population[0])

        # Create a new population using crossover and mutation
        new_population = []
        
        for i in range(0, len(population)//2, 1):
            parent1 = population[i]
            parent2 = population[i + 1] if i + 1 < len(population) else population[i]

            # Perform crossover to create two children
            child1, child2 = crossover.crossover(parent1, parent2)
            child1.calculate_fitness()
            child2.calculate_fitness()

            # Perform mutation on the children if a random number is less than MUTATION_RANGE (0.05)
            
            """
            if random.random() < MUTATION_RANGE:
                child1 = mutation.mutation(child1)
                child2 = mutation.mutation(child2)
            """
            
            new_population.append(child1)
            new_population.append(child2)

        population = new_population

        # Sort population again after mutation
        population.sort(key=lambda x: x.fitness, reverse=True)

        print(f"Generation {generation}: Best fitness = {population[0].fitness}")
    else:
        print("Maximum generations reached without finding a solution.")    
    # Calculate average fitness every 10 generations
    avg_fitness = []
    for i in range(0, len(best_fitness), 10):
        avg = sum(best_fitness[i:i+10]) / len(best_fitness[i:i+10])
        avg_fitness.append(avg)
    avg_x = list(range(9, len(best_fitness), 10))
    if len(best_fitness) % 10 != 0:
        avg_x.append(len(best_fitness) - 1)

    # Calculate the maximum fitness achieved
    max_fitness_value = max(best_fitness) if best_fitness else 0

    # Plot the fitness of the best chromosomes (blue line)
    plt.plot(best_fitness, label='Best Fitness', color='blue')
    # Plot the average fitness every 10 generations (red line)
    plt.plot(avg_x, avg_fitness, label='Average Fitness (per 10)', color='red')
    # Plot a horizontal line for the maximum fitness achieved
    plt.axhline(y=max_fitness_value, color='green', linestyle='--', label='Max Fitness')
    plt.xlim(left=0)

    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Genetic Algorithm Fitness Over Generations')
    plt.legend()
    plt.show()
    return best_chromosomes[0] if best_chromosomes else None

    