import random
inp = open('input.txt', 'r')

n, t = map(int, inp.readline().split())



courses = []

for i in range(n):
    course = inp.readline().strip()
    courses.append(course)


#############################################
#Necessary function to get the output
#############################################

def make_chromosome(n, t):
    chromosomes = []

    for i in range(4): #taking 4 chromosomes
        chromosomes = []
        for i in range(t):
            segment = []
            for j in range(n):
                segment.append(random.choice([0, 1]))
            chromosomes.extend(segment)

    return chromosomes

# chromosomes = make_chromosome(n, t, courses)

# print(chromosomes)
#############################################
def get_population(n, t, size):
    populations = []
    for i in range(size):
        populations.append(make_chromosome(n, t, courses))
    return populations

populations = get_population(n, t, 4)
print(populations)

#############################################

def fitness(chromosome, n, t):
    overlap_penalty = 0
    consistency_penalty = 0

    #Overlap penalty
    for overlap in range(t):
        segment = []
        total = 0
        start = overlap * n
        end = (overlap + 1 * n)
        segment = chromosome[start:end]

        for i in segment:
            total += i
        
        if total > 1:
            overlap_penalty += total - 1

    
    # Consistency penalty
    for c in range(n):
        counter = 0

        for time in range(t):
            course_segment = chromosome[time * n : (time + 1) * n]
            counter+= course_segment[c]

        if counter != 1:
            consistency_penalty+=abs(counter-1)

    return -(overlap_penalty + consistency_penalty)

    

# print(fitness(chromosomes, n, t))
# exit()
###################################################

#select parent based on tournament selection
def parent_select(population, fitness):
    tournament_index = random.sample(range(len(population)), 2)
    if fitness[tournament_index[0]] > fitness[tournament_index[1]]:
        return population[tournament_index[0]]
    else:
        return population[tournament_index[1]]

    return 0

###################################################
#Crossover
def cross_over(parent1, parent2):
    cross_over_point = random.randint(0, len(parent1))

    first_child = parent1[:cross_over_point] + parent2[cross_over_point:]
    second_child = parent2[:cross_over_point] + parent1[cross_over_point:]

    return first_child, second_child

###################################################

#Mutation
def mutation(chromosome):
    mutation_point = random.randint(0, len(chromosome) - 1)
    chromosome[mutation_point] = 1 - chromosome[mutation_point]
    return chromosome
###################################################
#Genetic Algorithm

def genetic_algorithm(n, t, iteraion, population_size):
    population = get_population(n, t, 4)
    fittest_chromosome = None
    max_fitness = -999999999999999999999999

    for i in range(iteraion):
        fitnesses = []
        for chromosome in population:
            fitnesses.append(fitness(chromosome, n, t))

        
    for p in range(population_size):
        if fitnesses[p] > max_fitness:
            max_fitness = fitnesses[p]
            fittest_chromosome = population[p]
    
    new_population = []

    for _ in range(population_size):
        first_parent = parent_select(population, fitnesses)
        second_parent = parent_select(population, fitnesses)

        first_child, second_child = cross_over(first_parent, second_parent)

        mutated_first_child = mutation(first_child)
        mutated_second_child = mutation(second_child)

        new_population.append(mutated_first_child)

    overall_fitness = []

    for chromosome in population:
        overall_fitness.append(fitness(chromosome, n, t))

    print(max(overall_fitness))
    return fittest_chromosome

print(genetic_algorithm(n, t, 100, 4))
###################################################
#Part 2
###################################################

def two_point_crossover(parent1, parent2):
    crossover_point1 = random.randint(2, 4) # between 2 and 3 inclusive
    crossover_point2 = random.randint(6, 8) # between 6 and 7 inclusive
    first_child = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
    second_child = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:]

    return first_child, second_child

first_parent = make_chromosome(n, t, courses)
second_parent = make_chromosome(n, t, courses)

first_child, second_child = two_point_crossover(first_parent, second_parent)

print(f"First Parent: {first_parent} \nSecond Parent: {second_parent}")
print(f"First child: {first_child} \nSecond child: {second_child}")

        


