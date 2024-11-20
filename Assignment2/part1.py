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

def make_chromosome(n, t, courses):
    chromosomes = []

    for i in range(4): #taking 4 chromosomes
        chromosomes = []
        for i in range(t):
            segment = []
            for j in range(n):
                segment.append(random.choice([0, 1]))
            chromosomes.extend(segment)

    return chromosomes

chromosomes = make_chromosome(n, t, courses)

print(chromosomes)
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

    return abs(overlap_penalty + consistency_penalty)

    

print(fitness(chromosomes, n, t))
###################################################


        


