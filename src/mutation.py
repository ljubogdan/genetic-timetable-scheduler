# Mutation operations for genetic algorithms
import crossover
from chromosome import Chromosome
from constants import MUTATION_ATTEMPTS, NUM_OF_LECTURES, MUTATION_RATE_PER_CHROMOSOME
import random
from utils import find_lecture_duration

def mutation(chromosome):
    counter = 0
    #create temp genes for swapping
    temp = [list(gene) for gene in chromosome.genes]
    while counter != MUTATION_RATE_PER_CHROMOSOME:
        #successful_mutation will be 2 if both lectures can be successfully rotated
        successful_mutation = 0
        repeat_mutation = False
        lecture_index1 = random.randrange(1,NUM_OF_LECTURES) #randomly choses a lecture
        available_indices = [i for i in range(1, NUM_OF_LECTURES) if i != lecture_index1]
        lecture_index2 = random.choice(available_indices)
        
        for classroom in temp:
            for i, lecture in enumerate(classroom):
                if isinstance(lecture, tuple) and lecture[0] == lecture_index1:
                    #check if two indices are in same classroom
                    exists = any(isinstance(x, tuple) and x[0] == lecture_index2 for x in classroom)
                    if exists:
                        repeat_mutation = True
                        break
                    new_duration = find_lecture_duration(lecture_index2)
                    time_difference = lecture[1] - new_duration
                    
                    if time_difference > 0:
                        #difference is added to the first element in classroom because if it is added to any other pause, mutation does not make sense
                        classroom[0] = classroom[0] + time_difference 
                        # lecture[0] = lecture_index2
                        # lecture[1] = new_duration
                        classroom[i] = (lecture_index2, new_duration)
                        successful_mutation +=1
                    elif time_difference == 0:
                        #repeat process
                        repeat_mutation = True
                        break
                    else:
                        if classroom[0] < time_difference * (-1):
                            if classroom[-1] < time_difference * (-1):
                                repeat_mutation = True
                                break
                            else:
                                classroom[-1] = classroom[-1] - time_difference * (-1)
                                # lecture[0] = lecture_index2
                                # lecture[1] = new_duration
                                classroom[i] = (lecture_index2, new_duration)
                                successful_mutation += 1
                        else:
                            classroom[0] = classroom[0] - time_difference * (-1)
                            # lecture[0] = lecture_index2
                            # lecture[1] = new_duration
                            classroom[i] = (lecture_index2, new_duration)
                            successful_mutation += 1

                if isinstance(lecture,tuple) and lecture[0] == lecture_index2:
                    #check if two indices are in same classroom
                    exists = any(isinstance(x, tuple) and x[0] == lecture_index1 for x in classroom)
                    if exists:
                        repeat_mutation = True
                        break
                    
                    new_duration = find_lecture_duration(lecture_index1)
                    time_difference = lecture[1] - new_duration
                    
                    if time_difference > 0:
                        #difference is added to the first element in classroom because if it is added to any other pause, mutation does not make sense
                        classroom[0] = classroom[0] + time_difference 
                        # lecture[0] = lecture_index1
                        # lecture[1] = new_duration
                        classroom[i] = (lecture_index1, new_duration)
                        successful_mutation +=1
                    elif time_difference == 0:
                        #repeat process
                        repeat_mutation = True
                        break
                    else:
                        if classroom[0] < time_difference * (-1):
                            if classroom[-1] < time_difference * (-1):
                                repeat_mutation = True
                                break
                            else:
                                classroom[-1] = classroom[-1] - time_difference * (-1)
                                # lecture[0] = lecture_index1
                                # lecture[1] = new_duration
                                classroom[i] = (lecture_index1, new_duration)
                                successful_mutation += 1
                        else:
                            classroom[0] = classroom[0] - time_difference * (-1)
                            # lecture[0] = lecture_index1
                            # lecture[1] = new_duration
                            classroom[i] = (lecture_index1, new_duration)
                            successful_mutation += 1

            if repeat_mutation:
                #if 2 indices are in same classroom or time difference can not be subtracted random indices will be chosen again
                break
        if successful_mutation == 2:
            #successful mutation
            chromosome.genes = temp
            counter += 1
            
        #reset
        temp = [list(gene) for gene in chromosome.genes]

# def mutation(chromosome):
#     """
#     Perform mutation on a given chromosome.
#     This function randomly selects a gene in the chromosome and modifies it.
#     The modification is done by reorganizing gene within the same classroom
#     """

    
#     if not isinstance(chromosome, Chromosome):
#         raise TypeError("The chromosome must be an instance of the Chromosome class.")

#     if not chromosome.genes:
#         raise ValueError("The chromosome has no genes to mutate.")
    
#     for _ in range(MUTATION_ATTEMPTS):
#         random_gene_index = random.randint(0, len(chromosome.genes) - 1)

#         # Since every gene looks like this: [ int, tuple, int, ... , tuple, int ]
#         # We take 2 random int-s and swap their places

#         random_gene = chromosome.genes[random_gene_index]

#         if len(random_gene) < 3:
#             continue

#         # Select two random indices for the integers in the gene
#         int_indices = [i for i, x in enumerate(random_gene) if isinstance(x, int)]

#         if len(int_indices) < 2:
#             continue

#         index1, index2 = random.sample(int_indices, 2)

#         # Swap the two integers
#         random_gene[index1], random_gene[index2] = random_gene[index2], random_gene[index1]

#         # Update the gene in the chromosome
#         chromosome.genes[random_gene_index] = random_gene

#     # Recalculate fitness after mutation
    
#     chromosome.calculate_fitness()

#     return chromosome



    
