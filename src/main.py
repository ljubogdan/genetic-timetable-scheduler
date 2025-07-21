from utils import generate_population, map_lectures, convert_chromosome
from data_handler import read_rooms, read_lectures
from genetic_algorithm import genetic_algorithm
from visualize_chromosome import visualize_best_chromosome

def main():
    rooms = read_rooms()
    lectures = read_lectures() 
    map, mapped_lectures = map_lectures(lectures)
    population = generate_population(mapped_lectures)
    best_chromosome = genetic_algorithm(population)
    print("Best fitness : ", str(best_chromosome.fitness))
    print("----------------------------------------------   ---------------------------")
    converted_chromosome = convert_chromosome(best_chromosome, lectures)
    visualize_best_chromosome(converted_chromosome)

if __name__ == "__main__":
    main()