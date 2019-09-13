# Dijkstra algorithm calculate shortest distances from one node to all others 
# Source https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/

import heapq
def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
##############################################################################

# Adjacency matrix by line. Created by Prohorov Kirill
from metro_by_line import METRO # METRO dict
full_dist_matrix = {}
for start_station in METRO:
    full_dist_matrix[start_station] = calculate_distances(METRO, start_station)

# Not necessary run this algorithm every time. You can use dict saved to file.
import sys
import os
with open(os.path.join(sys.argv[1], "full_dist_matrix.py"), "w", encoding="utf-8") as f:
    f.write("METRO = {}".format(full_dist_matrix))