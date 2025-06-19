from helpers import calculate_ald
from data_handler import read_lectures

POPULATION_SIZE = 100
<<<<<<< HEAD
MUTATION_RATE = 0.1 * POPULATION_SIZE
MUTATION_RATE_PER_CHROMOSOME = 2 # 2*2 lectures in chromosome will be rotated
NUM_OF_LECTURES = 60
MAX_GENERATIONS = 600
=======
MUTATION_RANGE = 0.05
MAX_GENERATIONS = 1000
>>>>>>> parent of 2c97ed8 (update)
NUMBER_OF_DAYS = 5
NUMBER_OF_CLASSROOMS = 5  
MAX_TIME_IN_CLASSROOM = 720 #time in minutes between 07:00 - 19:00
MIN_PAUSE_TIME = 15
MIN_NUMBER_OF_LECTURES = 2
AVERAGE_LECTURE_DURATION = int(calculate_ald(read_lectures()))
MAX_TIME_BEFORE_FIRST_CLASS = MAX_TIME_IN_CLASSROOM - (MIN_NUMBER_OF_LECTURES * AVERAGE_LECTURE_DURATION + (MIN_NUMBER_OF_LECTURES - 1) * MIN_PAUSE_TIME)
MAX_ATTEMPTS = 100
CROSSOVER_ATTEMPTS = 50
MUTATION_ATTEMPTS = 15      
DEDUCTED_FITNESS = 300
                                    
                                  
