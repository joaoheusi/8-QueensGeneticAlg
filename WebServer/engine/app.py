import random
import statistics
import sys


MAX_NUMBER_OF_GENERATIONS = 10000


def generatePopulation(size):
    individuals = size[0]
    weights = size[1]
    population = []
    for i in range(individuals):
        newIndv= []
        nums = list(range(1,9))
        random.shuffle(nums)
        for x in range(weights):
            newIndv.append(nums.pop())
        population.append(newIndv)
    return population

def breeding(parents):
    parentA = parents[0]
    parentB = parents[1]
    checkSimilarities = [0]*len(parentA)
    for i in range(len(parentA)):
        if parentA[i]== parentB[i]:
            checkSimilarities[i] = parentA[i]

    nums = list(range(1,9))
    nums = list(set(nums) - set(checkSimilarities))
    random.shuffle(nums)
    for i in range(len(checkSimilarities)):
        if checkSimilarities[i] == 0:
            checkSimilarities[i] = nums.pop()
    return checkSimilarities

def mutation(population,mutationChance):
    new_population = []
    for individual in range(len(population)):
        newIndv= []
        nums = list(range(1,9))
        random.shuffle(nums)
        for x in range(1,9):
            newIndv.append(nums.pop())
        if random.random() < 0.1:
            new_population.append(newIndv)
        else:
            new_population.append(population[individual]) 
    return new_population

def avaluate_individual(individual):
    individualTuples = []
    for gene in range(len(individual)):
        single = (gene +1,individual[gene])
        individualTuples.append(single)
    hits = 0
    for individual in individualTuples:
        x = individual[0]
        y = individual[1]
        diagonalValues = []
        for n in range(1,8):
            diagonalValues.append((x-n,y-n))
            diagonalValues.append((x+n,y-n))
            diagonalValues.append((x-n,y+n))
            diagonalValues.append((x+n,y+n))
        for test in individualTuples:
            if test in diagonalValues:
                hits += 1
    return (1/(1+hits))

def takeSecond(elem):
    return elem[1]

def selectFittest(population):
    single_aval = []
    for individual in population:
        single_aval.append((individual,avaluate_individual(individual)))
    
    sorted_list = sorted(single_aval,key=takeSecond, reverse=True) 
    fitness = list(i[1] for i in sorted_list)
    mean_fitness = statistics.mean(fitness)
    #print(mean_fitness)
    fittest = list(i[0] for i in sorted_list )
    return fittest,fitness


def nextGeneration(population,size):
    fittest,fitness = selectFittest(population)
    parents = fittest[0:2]
    newPopulation = []
    newPopulation.append(fittest[0])
    newPopulation.append(fittest[1])
    for i in range(size - 2):
        newPopulation.append(breeding(parents))
    return newPopulation

def code_run(individuals = 16):

    
    numWeights = 8
    indivPerPopulation = individuals
    pop_size = (indivPerPopulation,numWeights)

    a = generatePopulation(pop_size)
    generation = 0
    population = a
    generation_mean_fitness = 0
    fittest_individual = 0
    while fittest_individual < 1 or fittest_individual >= MAX_NUMBER_OF_GENERATIONS :
        genFittest,genFitness = selectFittest(a)
        print('Generation: {}'.format(generation))
        print('Fittest Individual: {}, It\'s fitness: {}'.format(genFittest[0],genFitness[0]))
        fittest_individual = genFitness[0]
        generation_mean_fitness = statistics.mean(genFitness)
        print('Average Fitness: {}'.format(generation_mean_fitness))
        returnable = [generation,genFittest,genFitness,generation_mean_fitness]
        a = mutation(nextGeneration(a,pop_size[0]),0.1)
        generation += 1 
    return returnable


if __name__ == "__main__":
    if len(sys.argv) > 1:
        code_run(int(sys.argv[1]))
    else:
        code_run()