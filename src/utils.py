def map_lectures(lectures):
    # mapp example: {'Lecture 1': 1, 'Lecture 2': 2, ...}
    # mapped_lectures example: [(1, 30), (2, 60), ...]
    mapped_lectures, mapp = [], {}
    i = 1
    for lecture, duration in lectures:
        mapped_lectures.append((i, duration))
        mapp[lecture] = i
        i += 1
    return mapp, mapped_lectures 

def calculate_ald(lectures): # Average Lecture Duration
    total_duration = sum(duration for _, duration in lectures)
    return total_duration / len(lectures) if lectures else 0

from chromosome import Chromosome
from constants import *
import random

def generate_population(original_lectures):
    lectures = original_lectures[:]
    population = []

    for i in range(POPULATION_SIZE): 
        genes = []

        for j in range(NUMBER_OF_DAYS):
            day = []          

            for k in range(NUMBER_OF_CLASSROOMS):
                classroom, minutes = [], 0
                number_of_lectures = MIN_NUMBER_OF_LECTURES

                # Add a random time before the first class
                time_before_first_class = random.randrange(0, MAX_TIME_BEFORE_FIRST_CLASS)
                classroom.append(time_before_first_class)
                minutes += time_before_first_class

                while minutes <= MAX_TIME_IN_CLASSROOM and len(lectures) > 0:
                    #adding random lecture
                    indicator = False

                    attempts = 0   
                    while not indicator and attempts < MAX_ATTEMPTS:
                        attempts += 1
                        
                        random_lecture_index = random.randrange(0,len(lectures))
                        random_lecture = lectures[random_lecture_index]

                        #if minimum of lectures is not satisfied, another lecture is chosen
                        if (minutes + random_lecture[1] >= MAX_TIME_IN_CLASSROOM) and number_of_lectures != 0:
                            continue
                        elif (minutes + random_lecture[1] >= MAX_TIME_IN_CLASSROOM) and number_of_lectures == 0:
                            indicator = True
                        else:
                            break

                    if attempts >= MAX_ATTEMPTS:
                        indicator = True
                    if indicator == True:
                        break

                    classroom.append(random_lecture)
                    number_of_lectures -= 1
                    minutes += random_lecture[1] 
                    
                    # Removing the lecture from the list to avoid duplicates in the same classroom
                    lectures[random_lecture_index] = lectures[-1] 
                    lectures.pop()

                    #print(len(lectures), "lectures left in the list")

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

        #adding remaining lectures 
        while lectures:
            lecture = lectures[-1]
            placed = False

            for j in range(NUMBER_OF_DAYS):
                for k in range(NUMBER_OF_CLASSROOMS):
                    classroom = genes[j][k]

                    #finding enough long pause
                    for idx, elem in enumerate(classroom):
                        if isinstance(elem, int):  # pause
                            if elem >= lecture[1] + 2 * MIN_PAUSE_TIME:
                    
                                pause_before = MIN_PAUSE_TIME
                                pause_after = elem - lecture[1] - MIN_PAUSE_TIME

                                #change that pause
                                classroom[idx:idx+1] = [pause_before, lecture, pause_after]

                                lectures.pop()
                                placed = True
                                break
                    if placed:
                        break
                if placed:
                    break

            if not placed:
                raise Exception(f"Lekciju {lecture} nije moguće ubaciti!")
        print("remaining lectures : " + str(len(lectures)))    
        
        # Merging all list of classroms into a single list
        new_genes = [classroom for day in genes for classroom in day]

        chromosome = Chromosome(new_genes)
        population.append(chromosome)

        lectures = original_lectures[:]

    return population