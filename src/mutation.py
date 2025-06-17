# Mutation operations for genetic algorithms
import crossover
from chromosome import Chromosome
from constants import MUTATION_ATTEMPTS

import random

def mutation(chromosome):
    """
    Perform mutation on a given chromosome.
    This function randomly selects a gene in the chromosome and modifies it.
    The modification is done by reorganizing gene within the same classroom
    """

    """
    if not isinstance(chromosome, Chromosome):
        raise TypeError("The chromosome must be an instance of the Chromosome class.")

    if not chromosome.genes:
        raise ValueError("The chromosome has no genes to mutate.")
    
    for _ in range(MUTATION_ATTEMPTS):
        random_gene_index = random.randint(0, len(chromosome.genes) - 1)

        # Since every gene looks like this: [ int, tuple, int, ... , tuple, int ]
        # We take 2 random int-s and swap their places

        random_gene = chromosome.genes[random_gene_index]

        if len(random_gene) < 3:
            continue

        # Select two random indices for the integers in the gene
        int_indices = [i for i, x in enumerate(random_gene) if isinstance(x, int)]

        if len(int_indices) < 2:
            continue

        index1, index2 = random.sample(int_indices, 2)

        # Swap the two integers
        random_gene[index1], random_gene[index2] = random_gene[index2], random_gene[index1]

        # Update the gene in the chromosome
        chromosome.genes[random_gene_index] = random_gene

    # Recalculate fitness after mutation
    """
    chromosome.calculate_fitness()

    return chromosome



    
