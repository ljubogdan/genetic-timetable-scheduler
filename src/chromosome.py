
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
        

        
        

