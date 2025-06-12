from src.data_handler import read_rooms, read_lectures

class Chromosome:
    def __init__(self, genes=None):
        self.genes = genes if genes is not None else []
        self.fitness = 0.0

    def calculate_fitness(self):
        pass

