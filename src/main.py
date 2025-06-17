from utils import generate_population, map_lectures
from data_handler import read_rooms, read_lectures
from crossover import crossover
from mutation import mutation

def main():
    rooms = read_rooms()
    lectures = read_lectures() 
    map, mapped_lectures = map_lectures(lectures)
    #print(map)
    #print(mapped_lectures)
    #print (len(mapped_lectures))
    population = generate_population(mapped_lectures)
    for chromosome in population:
        print()
        print(chromosome)

    print()
    child1, child2 = crossover(population[0], population[1])

    print()
    print("Child 1 after crossover:")
    print(child1)
    print("Child 2 after crossover:")
    print(child2)

    print()
    child1.calculate_fitness()
    print(child1.fitness)
    mutated_child1 = mutation(child1)
    print("Child 1 after mutation:")
    print(mutated_child1)
    print(mutated_child1.fitness)
    

if __name__ == "__main__":
    main()