
class Chromosome:
    def __init__(self, genes=None):
        self.genes = genes if genes is not None else []
        self.fitness = 0.0

    def __str__(self):
        return str(self.genes)
    
    def calculate_fitness(self):
        pass

