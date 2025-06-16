from utils import generate_population, map_lectures
from data_handler import read_rooms, read_lectures

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

if __name__ == "__main__":
    main()