from utils import generate_population, map_lectures
from data_handler import read_rooms, read_lectures
from crossover import crossover
from mutation import mutation
from genetic_algorithm import genetic_algorithm

def main():
    rooms = read_rooms()
    lectures = read_lectures() 
    map, mapped_lectures = map_lectures(lectures)

    population = generate_population(mapped_lectures)

    #genetic_algorithm(population)
    print("HROMOZOM PRIJE MUTIRANJA")
    print("-------------------------------------------------------")
    print(population[0])
    print("HROMOZOM POSLIJE MUTIRANJA")
    print("-------------------------------------------------------")
    mutation(population[0])
    print(population[0])



if __name__ == "__main__":
    main()