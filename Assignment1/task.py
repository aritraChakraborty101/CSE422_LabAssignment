from queue import PriorityQueue
inp = open("Input file.txt", "r")

heuristics = {}
graph = {}

def create_neighbours(neighbours):
    main_neighbours = []
    for neighbour in range(0, len(neighbours), 2):
        main_neighbours.append((neighbours[neighbour], int(neighbours[neighbour + 1])))
    return main_neighbours

while True:
    line = inp.readline()
    if not line:
        break
    line = line.split()
    node, heuristics_value, neighbours = line[0], line[1], line[2:]
    heuristics[node] = int(heuristics_value)
    neighbours = create_neighbours(neighbours)
    graph[node] = neighbours



def optimal_path(parent, current, g_costs, start):
    path = []
    path.append(current)
    while current is not start:
        current = parent[current]
        path.append(current)
    path.reverse()
    return path, g_costs[path[-1]]

# for testing purposes the graph and heuristics are hardcoded
# the graph and heuristics are read from the file

# graph = {
#     'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
#     'Craiova': [('Dobreta', 120), ('RimnicuVilcea', 146), ('Pitesti', 138)],
#     'Eforie': [('Hirsova', 86)],
#     'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
#     'Giurgiu': [('Bucharest', 90)],
#     'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
#     'Neamt': [('lasi', 87)],
#     'Sibiu': [('Oradea', 151), ('Arad', 140), ('RimnicuVilcea', 80), ('Fagaras', 99)],
#     'Oradea': [('Zerind', 71), ('Sibiu', 151)],
#     'Pitesti': [('RimnicuVilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
#     'RimnicuVilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
#     'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
#     'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
#     'lasi': [('Vaslui', 92), ('Neamt', 87)],
#     'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
#     'Timisoara': [('Arad', 118), ('Lugoj', 111)],
#     'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
#     'Vaslui': [('Urziceni', 142), ('lasi', 92)],
#     'Zerind': [('Oradea', 71), ('Arad', 75)],
#     'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)]
# }


# heuristics = {
#     'Arad': 366, 'Craiova': 160, 'Eforie': 161, 'Fagaras': 176,
#     'Giurgiu': 77, 'Mehadia': 241, 'Neamt': 234, 'Sibiu': 253,
#     'Oradea': 380, 'Pitesti': 100, 'RimnicuVilcea': 193, 'Dobreta': 242,
#     'Hirsova': 151, 'lasi': 226, 'Lugoj': 244, 'Timisoara': 329,
#     'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374, 'Bucharest': 0
# }




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
else:
    result = "The path is "
    for node in path:
        result += node + " -> "
        
    print(result[0:-4])
    print("The cost is:", cost)






