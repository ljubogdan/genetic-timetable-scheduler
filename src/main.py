from data_handler import read_rooms, read_lectures, map_lectures
from chromosome import Chromosome
from constants import  MAX_ATTEMPTS, NUMBER_OF_DAYS, NUMBER_OF_CLASSROOMS, AVERAGE_LECTURE_DURATION,MIN_NUMBER_OF_LECTURES, POPULATION_SIZE, MAX_TIME_IN_CLASSROOM, MIN_PAUSE_TIME,MAX_TIME_BEFORE_FIRST_CLASS
import random

def generate_population(lectures):
    population = []
    for i in range(POPULATION_SIZE): #for every chromosome makes list of days
        genes = []
        for j in range(NUMBER_OF_DAYS): #for every day in chromosome makes list of classrooms
            day = []          
            for k in range(NUMBER_OF_CLASSROOMS): #for every classroom makes list of lectures 
                classroom = []
                minutes = 0
                number_of_lectures = MIN_NUMBER_OF_LECTURES
                #adding time between 07:00 and first lecture
                time_before_first_class = random.randrange(0,MAX_TIME_BEFORE_FIRST_CLASS)
                classroom.append(time_before_first_class)
                minutes += time_before_first_class
                while minutes <= MAX_TIME_IN_CLASSROOM:
                    #adding random lecture
                    indicator = False

                    attempts = 0   
                    while indicator != True and attempts < MAX_ATTEMPTS:
                        attempts += 1
                        random_lecture_index = random.randrange(0,len(lectures))
                        #if minimum of lectures is not satisfied, another lecture is chosen
                        if (minutes + lectures[random_lecture_index][1] >= MAX_TIME_IN_CLASSROOM) and number_of_lectures != 0 :
                            continue
                        elif (minutes + lectures[random_lecture_index][1] >= MAX_TIME_IN_CLASSROOM) and number_of_lectures == 0:
                            indicator = True
                        else:
                            break
                    if attempts >= MAX_ATTEMPTS:
                        indicator = True
                    if indicator == True:
                        break
                    classroom.append(lectures[random_lecture_index])
                    number_of_lectures -= 1
                    minutes += lectures[random_lecture_index][1] 
                    #adding random pause
                    if number_of_lectures == 0: #if minimum of lectures is satisfied
                        upper_limit_pause =  MAX_TIME_IN_CLASSROOM - minutes
                    elif number_of_lectures - 1 >= 0:
                        upper_limit_pause =  MAX_TIME_IN_CLASSROOM - minutes - (number_of_lectures * AVERAGE_LECTURE_DURATION + (number_of_lectures - 1) * MIN_PAUSE_TIME)
                    else:
                        upper_limit_pause =  MAX_TIME_IN_CLASSROOM - minutes - number_of_lectures * AVERAGE_LECTURE_DURATION 
                    
                    if upper_limit_pause > MIN_PAUSE_TIME:
                        pause = random.randrange(MIN_PAUSE_TIME, upper_limit_pause)
                        minutes += pause
                        classroom.append(pause)
                    else:
                        pause = MIN_PAUSE_TIME
                        if minutes + pause >=MAX_TIME_IN_CLASSROOM:
                            break
                        else:
                            minutes += pause
                            classroom.append(pause)
                #if the last element in list was lecture, remaining time is time between the last lecture and 19:00
                #if the last element in list was pause, remaining time is then added to pause
                last_element = classroom[-1]
                if isinstance(last_element, int):
                    remaining_time = MAX_TIME_IN_CLASSROOM - minutes
                    classroom[-1] = last_element + remaining_time
                elif isinstance(last_element, tuple):
                    remaining_time = MAX_TIME_IN_CLASSROOM - minutes
                    classroom.append(remaining_time)
                    
                day.append(classroom)
            genes.append(day)   
        chromosome = Chromosome(genes)
        population.append(chromosome)
    return population
                

def main():
    rooms = read_rooms()
    lectures = read_lectures() 
    map, mapped_lectures = map_lectures(lectures)
    #print(map)
    #print(mapped_lectures)
    #print (len(mapped_lectures))
    population = generate_population(mapped_lectures)
    for chromosome in population:
        print(chromosome)

if __name__ == "__main__":
    main()