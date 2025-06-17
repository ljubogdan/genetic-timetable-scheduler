from constants import DEDUCTED_FITNESS, MIN_PAUSE_TIME
class Chromosome:
    def __init__(self, genes=None):
        self.genes = genes if genes is not None else []
        self.fitness = 0.0

    def __str__(self):
        return str(self.genes)
    
    def calculate_fitness(self):
        """
        Calculate the fitness of the chromosome.
        The fitness is calculated as the sum of all pauses at the end and the beginning of each classroom.
        """

        self.fitness = 0.0
        for classroom in self.genes:
            if isinstance(classroom[0], int):
                self.fitness += classroom[0]
            if isinstance(classroom[-1], int):
                self.fitness += classroom[-1]
        
        # Go through all genes throughout the chromosome
        # If there is a int value between two tuples (left and right are tuples) that is below MIN_PAUSE_TIME, deduct points
        # target only int that are not on index 0 or -1

        for classroom in self.genes:
            for i in range(1, len(classroom) - 1):
                if isinstance(classroom[i], int) and classroom[i] < MIN_PAUSE_TIME:
                    # Deduct points for each pause that is less than MIN_PAUSE_TIME
                    self.fitness -= DEDUCTED_FITNESS