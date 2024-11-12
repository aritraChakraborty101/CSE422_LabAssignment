from queue import PriorityQueue
inp = open("Input file.txt", "r")

heuristics = {}
graph = {}

def create_neighbours(neighbours):
    main_neighbours = []
    for neighbour in range(0, len(neighbours), 2):
        main_neighbours.append((neighbours[neighbour], int(neighbours[neighbour + 1])))
    return main_neighbours

def optimal_path(parent, current, g_costs, start):
    path = []
    path.append(current)
    while current is not start:
        current = parent[current]
        path.append(current)
    path.reverse()
    return path, g_costs[path[-1]]


while True:
    line = inp.readline()
    if not line:
        break
    line = line.split()
    node, heuristics_value, neighbours = line[0], line[1], line[2:]
    heuristics[node] = int(heuristics_value)
    neighbours = create_neighbours(neighbours)
    graph[node] = neighbours




def a_star_search(start, goal, graph):
    fringe = PriorityQueue()
    fringe.put((0, start)) 
    parent = {}
    visited = {start: 0}
    f_costs = {start: heuristics[start]}

    while not fringe.empty():
        cost, current = fringe.get()
        if current == goal:
            return optimal_path(parent, current, visited, start)
        if current in graph: 
            for neighbor, distance in graph[current]:
                g_n = visited[current] + distance
                if neighbor not in visited or g_n < visited[neighbor]:
                    parent[neighbor] = current
                    visited[neighbor] = g_n
                    f_costs[neighbor] = g_n + heuristics[neighbor]
                    fringe.put((f_costs[neighbor], neighbor))

    return None, None



path, cost = a_star_search('Arad', 'Bucharest', graph)

if path is None:
    print("No path found")
    inp.close()
else:
    result = "The path is "
    for node in path:
        result += node + " -> "
        
    print(result[0:-4])
    print("The cost is:", cost)

    inp.close()