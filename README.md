# Genetic Algorithm for Lecture Scheduling

## Introduction
This project implements a genetic algorithm to automatically generate lecture and lab schedules over five weekdays (07:00–19:00) with a mandatory 15-minute break between consecutive sessions in the same room. Each event is assigned to a day, room, and time slot, and the fitness function maximizes the sum of products of the pre-first and post-last break durations for each room on each day.

## Program Structure
In **main.py**, the process is orchestrated by calling:
- `read_rooms()` and `read_lectures()` from **data_handler.py**
- `map_lectures()` and `generate_population()` from **utils.py**
- `genetic_algorithm()` from **genetic_algorithm.py**, which returns `best_chromosome`.

**constants.py** defines all parameters:
`POPULATION_SIZE`, `MAX_GENERATIONS`, `ELITISM_RATE`, `MUTATION_RANGE`, `MUTATION_RATE_PER_CHROMOSOME`, `STAGNATION_THRESHOLD`, `SHAKEUP_RATIO`, `NUMBER_OF_DAYS`, `NUMBER_OF_CLASSROOMS`, `MAX_TIME_IN_CLASSROOM`, `MIN_PAUSE_TIME`, `MIN_NUMBER_OF_LECTURES`, `AVERAGE_LECTURE_DURATION`, `MAX_TIME_BEFORE_FIRST_CLASS`, `MAX_ATTEMPTS`, `CROSSOVER_ATTEMPTS`, `MUTATION_ATTEMPTS`, `DEDUCTED_FITNESS`, `NUM_OF_LECTURES`.

**data_handler.py** parses input with `read_rooms()` and `read_lectures()`.  
**utils.py** provides `map_lectures()`, `generate_population()`, and `find_lecture_duration()`.  
**chromosome.py** defines the `Chromosome` class with `genes` and `calculate_fitness()`.  
**selection.py** implements `rank_selection()` and `tournament_selection()`.  
**crossover.py** defines `crossover()` with limited attempts.  
**mutation.py** defines `mutation()` with rate and attempt limits.  
**genetic_algorithm.py** runs the GA loop: evaluation, selection with elitism and shakeup, crossover, mutation, tracking `best_fitness`, and returning the best solution.

## Mutation and Crossover Operators
The `crossover(parent1, parent2)` function tries up to `CROSSOVER_ATTEMPTS` times to swap two lecture assignments between parents, adjusting break times to maintain validity. Once a valid swap is found, it produces two offspring. The `mutation(chromosome)` function performs up to `MUTATION_RATE_PER_CHROMOSOME` successful swaps of lecture indices, each constrained by `MUTATION_ATTEMPTS`, updating `genes` and recalculating fitness.

## Selection Strategy
`rank_selection(population)` sorts individuals by fitness, assigns rank-based scores, then selects adjacent pairs for crossover. Alternatively, `tournament_selection(population, k=10)` chooses the best out of k random candidates.

## Parameter Choices
Parameters balance exploration and performance:
- POPULATION_SIZE = 100
- MAX_GENERATIONS = 600
- ELITISM_RATE = 10
- STAGNATION_THRESHOLD = 10
- SHAKEUP_RATIO = 0.9
- CROSSOVER_ATTEMPTS = 50
- MUTATION_RATE_PER_CHROMOSOME = 6
- MUTATION_ATTEMPTS = 15
- MIN_PAUSE_TIME = 15 minutes

## Problem Constraints
Scheduling spans five workdays and a fixed set of classrooms within 07:00–19:00 (720 minutes). Each event must fit within that interval and respect a 15-minute minimum break (`MIN_PAUSE_TIME`). Input includes `NUM_OF_LECTURES = 60` events, and at least two lectures per room per day.

## Algorithm Results
The GA reached a final fitness of **1,066,940** at generation 597. Rapid growth to ~99% of that value occurred by generation 200, followed by slower, stepwise improvements and a final shakeup that escaped a local optimum near the end. Reducing the number of generations to 300–400 and triggering shakeup earlier (e.g., at 5 stagnating generations) cuts runtime, while slight increases in mutation rate or decreases in elitism introduce more diversity.

## Authors
- Bogdan Ljubinković
- Andjela Broćeta

## License
MIT
