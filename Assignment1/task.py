from queue import PriorityQueue
inp = open("Input file.txt", "r")

heuristics = {}
graph = {}

def create_neighbours(neighbours):
    main_neighbours = []
    for neighbour in range(0, len(neighbours), 2):
        main_neighbours.append((neighbours[neighbour], int(neighbours[neighbour + 1])))
    return main_neighbours

def optimal_path(parent, current, g_costs):
    path = []
    path.append(current)
    while current in parent:
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
            return optimal_path(parent, current, visited)
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
result = "The path is "
for node in path:
    result += node + " -> "
    
print(result[0:-4])
print("The cost is:", cost)











#----------------------------------------------

# #for all nodes in the graph get all the parent nodes
# def get_g_value(graph, start, current):
#     # Dictionary to store the minimum path cost to each node from the start node
#     path_costs = {node: float('inf') for node in graph}
#     path_costs[start] = 0  # Cost from start to start is zero
    
#     # Frontier set initialized with the start node
#     frontier = [(start, 0)]
    
#     while frontier:
#         # Get the current node and its cost
#         node, cost = frontier.pop(0)
        
#         # Update cost for each neighbor if we found a cheaper path
#         for neighbor, edge_cost in graph[node]:
#             new_cost = cost + int(edge_cost)
#             if new_cost < path_costs[neighbor]:
#                 path_costs[neighbor] = new_cost
#                 frontier.append((neighbor, new_cost))
    
#     return path_costs[current]

# print(get_g_value(graph, "Arad", "Zerind"))

# def get_h_value(node):
#     for key, value in heuristics_distance:
#         if key == node:
#             return int(value)




# print("--------------------")
# def a_star(graph, start, goal):
#     return None




# print(a_star(graph, "Arad", "Bucharest"))


# print(heuristics_distance)
# print("--------------------")

# # for key, value in graph.items():
# #     print(key, value)

# def get_neighbours(n, t):
#     for n in t:
#         return t[n]
#     else:
#         return None
    


# def a_star(graph, start, goal):
#     unexplored_nodes = [start]
#     explored_nodes = []
#     dist = {}
#     parent = {}
#     dist[start] = 0
#     parent[start] = start

#     while len(unexplored_nodes) > 0:
#         n = None
#         for l in unexplored_nodes:
#             if n is None or dist[l] + heuristics_distance[l] < dist[n] + heuristics_distance[n]:
#                 n = l
        
#         if n == goal or graph[n] == None:
#             pass

#         else:
#             for (j, w) in get_neighbours(n, graph):
#                 if j not in unexplored_nodes and j not in explored_nodes:
#                     unexplored_nodes.append(j)
#                     parent[j] = n
#                     dist[j] = dist[n] + int(w)
#                 else:
#                     if dist[j] > dist[n] + int(w):
#                         dist[j] = dist[n] + int(w)
#                         parent[j] = n
#                         if j in explored_nodes:
#                             explored_nodes.remove(j)
#                             unexplored_nodes.append(j)

#             if n == goal:
#                 path = []
#                 while parent[n] != n:
#                     path.append(n)
#                     n = parent[n]

#                 path.append(start)
#                 path.reverse()

#                 return path
            
#             unexplored_nodes.remove(n)
#             explored_nodes.append(n)



# a = a_star(graph, "Arad", "Bucharest")
# print(a)

