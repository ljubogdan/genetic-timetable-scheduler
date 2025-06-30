# Selection methods for population-based training.
import random
def rank_selection(population):
    population.sort(key=lambda x: x.fitness, reverse=True)
    
    ranked_population = []
    rank = len(population)

    for chromosome in population: 
        rand = random.random() #random number 0-1 
        score = rand * rank
        ranked_population.append((chromosome, score))
        
        rank -= 1

    ranked_population.sort(key=lambda x: x[1], reverse=True) #sorted according to score

    sorted_population = [chrom for chrom, _ in ranked_population] #new list containing only sorted chromosomes
    return sorted_population


def tournament_selection(population, k=10):
    #from sample of random chromosomes chooses best fitness chromosome 
    tournament = random.sample(population, k)
    winner = max(tournament, key=lambda x: x.fitness)
    return winner
