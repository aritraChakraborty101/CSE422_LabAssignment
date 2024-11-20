n = 3
t = 3
courses = ['C1', 'C2', 'C3']


def fitness(n, t, courses):
    chromosome = [[1,1,0],[1,1,0],[0,1,0]]

    overlap_penalty = 0
    consistency_penalty = 0

    # Overlap penalty
    for i in range(t):
        segment = []
        for j in range(n):
            segment.append(chromosome[i][j])
        scheduled_courses = segment.count(1)
        if scheduled_courses > 1:
            overlap_penalty += scheduled_courses - 1
    
    # Consistency penalty
    for c in range(n):
        counter = 0
        temp = []
        for ti in range(t):
            temp.append(chromosome[c + ti * n])
            counter+= temp[ti]
        if counter != 1:
            consistency_penalty+=abs(counter - 1)

    return abs(overlap_penalty + consistency_penalty)


print(fitness(n, t, courses))