# Methods for crossover operations in genetic algorithms.

from chromosome import Chromosome
from constants import CROSSOVER_ATTEMPTS
import random

def crossover(parent1, parent2):
    # Returns two children created by crossover between two parents.
    if not isinstance(parent1, Chromosome) or not isinstance(parent2, Chromosome):
        raise TypeError("Both parents must be instances of the Chromosome class.")

    if len(parent1.genes) != len(parent2.genes):
        raise ValueError("Parents must have the same number of genes for crossover.")
    
    child1 = Chromosome(genes=parent1.genes[:])
    child2 = Chromosome(genes=parent2.genes[:])

    # Gene example:
    """
    [[346, (49, 180), 60, (55, 90), 44], [178, (16, 120), 275, (57, 120), 27], [103, (56, 180), 109, (46, 90), 132, (10, 60), 46], [472, (38, 180), 15, (6, 30), 23], [193, (51, 120), 38, (9, 30), 221, (13, 60), 58], [393, (54, 90), 19, (7, 30), 65, (20, 120), 3], [46, (30, 90), 17, (11, 180), 152, (34, 30), 205], [157, (48, 60), 155, (19, 180), 168], [407, (27, 180), 17, (58, 60), 56], [387, (47, 180), 18, (35, 120), 15], [17, (39, 120), 153, (31, 180), 49, (2, 120), 81], [20, (15, 120), 105, (14, 180), 82, (60, 60), 84, (32, 30), 39], [295, (45, 180), 105, (8, 90), 50], [431, (23, 60), 63, (52, 120), 46], [318, (22, 120), 164, (28, 90), 28], [442, (17, 180), 15, (42, 30), 53], [363, (26, 30), 192, (18, 60), 75], [11, (44, 180), 173, (12, 90), 83, (59, 180), 3], [13, (33, 180), 139, (40, 120), 62, (36, 30), 176], [274, (43, 180), 18, (21, 180), 68], [394, (29, 180), 28, (24, 60), 58], [349, (50, 90), 111, (25, 60), 110], [376, (4, 180), 23, (41, 120), 21], [344, (3, 120), 79, (5, 90), 87], [95, (53, 180), 16, (37, 180), 39, (1, 180), 30]]
    """

    # Where integer values represent pauses and tuples represent lectures
    # We will perform lectures swapping between parents (if possible because of leftover time in classroom)
    # For instance 30 tries to swap lectures between parents
    # Since each lecture needs to appear once and only once in a classroom
    # we need to ensure that the swap does not violate this condition
    # we first find 2 donor lectures from child1
    # and 2 recipient lectures from child2
    # where donor_lecture1 = receipient_lecture2 
    # and donor_lecture2 = receipient_lecture1

    # child1 is donor 
    # child2 is recipient

    for i in range(CROSSOVER_ATTEMPTS):
        donor_lecture1 = None
        donor_lecture2 = None
        recipient_lecture1 = None
        recipient_lecture2 = None

        index_of_dl1_classroom = None
        index_of_dl2_classroom = None
        index_of_rl1_classroom = None
        index_of_rl2_classroom = None

        index_of_dl1_lecture = None
        index_of_dl2_lecture = None
        index_of_rl1_lecture = None
        index_of_rl2_lecture = None

        while donor_lecture1 is None:
            random_classroom = random.choice(child1.genes)
            random_lecture = random.choice(random_classroom)
            if isinstance(random_lecture, tuple):
                donor_lecture1 = random_lecture
                index_of_dl1_classroom = child1.genes.index(random_classroom)
                index_of_dl1_lecture = random_classroom.index(random_lecture)
                break
        
        # Ensure that we do not select the same lecture again
        while donor_lecture2 is None:
            random_classroom = random.choice(child1.genes)
            random_lecture = random.choice(random_classroom)
            if isinstance(random_lecture, tuple) and random_lecture != donor_lecture1:
                donor_lecture2 = random_lecture
                index_of_dl2_classroom = child1.genes.index(random_classroom)
                index_of_dl2_lecture = random_classroom.index(random_lecture)
                break
        
        # receipent_lecture1 should be the same as donor_lecture2, and vice versa
        for classroom in child2.genes:
            for lecture in classroom:
                if isinstance(lecture, tuple):
                    if lecture == donor_lecture2:
                        recipient_lecture1 = lecture
                        index_of_rl1_classroom = child2.genes.index(classroom)
                        index_of_rl1_lecture = classroom.index(lecture)
                    elif lecture == donor_lecture1:
                        recipient_lecture2 = lecture
                        index_of_rl2_classroom = child2.genes.index(classroom)
                        index_of_rl2_lecture = classroom.index(lecture)

        # If we found all lectures, we TRY to swap them
        # After the swap, we need to correct times
        if (donor_lecture1 is not None and donor_lecture2 is not None and 
            recipient_lecture1 is not None and recipient_lecture2 is not None):
            
            # Before swap calculate donors' and recipients' times
            donor1_time = child1.genes[index_of_dl1_classroom][index_of_dl1_lecture][1]
            donor2_time = child1.genes[index_of_dl2_classroom][index_of_dl2_lecture][1]
            recipient1_time = child2.genes[index_of_rl1_classroom][index_of_rl1_lecture][1]
            recipient2_time = child2.genes[index_of_rl2_classroom][index_of_rl2_lecture][1]

            # Calculate time difference
            time_difference1 = donor1_time - recipient1_time # positive if donor1_time > recipient1_time, so donor has more free time
            time_difference2 = donor2_time - recipient2_time 

            # ========== Swap ============

            # Create temp genes for swapping
            temp_c1g = child1.genes[:]
            temp_c2g = child2.genes[:]

            temp_c1g[index_of_dl1_classroom][index_of_dl1_lecture] = recipient_lecture1
            temp_c1g[index_of_dl2_classroom][index_of_dl2_lecture] = recipient_lecture2
            temp_c2g[index_of_rl1_classroom][index_of_rl1_lecture] = donor_lecture1
            temp_c2g[index_of_rl2_classroom][index_of_rl2_lecture] = donor_lecture2

            # ========== Correct times ============

            # If time difference is positive, we need to subtract it from recipient's free time
            # And add it to donor's free time
            # Every time we take a random odd index in lecture list (that represents time) type int

            random_d1_time_index = random.randrange(0, len(child1.genes[index_of_dl1_classroom]), 2)
            random_d2_time_index = random.randrange(0, len(child1.genes[index_of_dl2_classroom]), 2)
            random_r1_time_index = random.randrange(0, len(child2.genes[index_of_rl1_classroom]), 2)
            random_r2_time_index = random.randrange(0, len(child2.genes[index_of_rl2_classroom]), 2)

            if time_difference1 > 0:
                temp_c1g[index_of_dl1_classroom][random_d1_time_index] += time_difference1
                temp_c2g[index_of_rl1_classroom][random_r1_time_index] -= time_difference1

                if temp_c2g[index_of_rl1_classroom][random_r1_time_index] < 0:
                    print("Negative time in recipient's classroom after crossover, skipping this attempt.")

                    # revert changes
                    temp_c1g[index_of_dl1_classroom][random_d1_time_index] -= time_difference1
                    temp_c2g[index_of_rl1_classroom][random_r1_time_index] += time_difference1
                    continue

            elif time_difference1 < 0:
                temp_c1g[index_of_dl1_classroom][random_d1_time_index] += time_difference1
                temp_c2g[index_of_rl1_classroom][random_r1_time_index] -= time_difference1

                if temp_c1g[index_of_dl1_classroom][random_d1_time_index] < 0:
                    print("Negative time in donor's classroom after crossover, skipping this attempt.")

                    # revert changes
                    temp_c1g[index_of_dl1_classroom][random_d1_time_index] -= time_difference1
                    temp_c2g[index_of_rl1_classroom][random_r1_time_index] += time_difference1
                    continue

            if time_difference2 > 0:
                temp_c1g[index_of_dl2_classroom][random_d2_time_index] += time_difference2
                temp_c2g[index_of_rl2_classroom][random_r2_time_index] -= time_difference2

                if temp_c2g[index_of_rl2_classroom][random_r2_time_index] < 0:
                    print("Negative time in recipient's classroom after crossover, skipping this attempt.")

                    # revert changes
                    temp_c1g[index_of_dl2_classroom][random_d2_time_index] -= time_difference2
                    temp_c2g[index_of_rl2_classroom][random_r2_time_index] += time_difference2
                    continue
                
            elif time_difference2 < 0:
                temp_c1g[index_of_dl2_classroom][random_d2_time_index] += time_difference2
                temp_c2g[index_of_rl2_classroom][random_r2_time_index] -= time_difference2

                if temp_c1g[index_of_dl2_classroom][random_d2_time_index] < 0:
                    print("Negative time in donor's classroom after crossover, skipping this attempt.")

                    # revert changes
                    temp_c1g[index_of_dl2_classroom][random_d2_time_index] -= time_difference2
                    temp_c2g[index_of_rl2_classroom][random_r2_time_index] += time_difference2
                    continue
            
            # If we reach this point, we can safely assign new genes to children
            child1.genes = temp_c1g
            child2.genes = temp_c2g
            print(f"Crossover successful on attempt {i + 1}.")
        else:
            print(f"Attempt {i + 1} failed, not all lectures found for crossover.")
    return child1, child2
            
