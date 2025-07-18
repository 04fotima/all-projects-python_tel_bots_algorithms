import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None

    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None

    def isEmpty(self):
        return len(self.stack) == 0


k = sys.maxsize


def DFS(g):
    st1 = Stack()
    visited = [True, False, False, False, False, False]
    i = 0
    st1.push(i)
    while not st1.isEmpty():
        d = st1.top()
        st1.pop()
        print(d + 1, end=' ')
        for j in range(6):
            if g[d][j] < k and not visited[j]:
                st1.push(j)
                visited[j] = True
    print()


def minMetka(metka, visited):
    m = k
    n = 0
    for i in range(len(metka)):
        if m > metka[i] and not visited[i]:
            m = metka[i]
            n = i
    return n


def dijkstra(g, src):
    src -= 1
    metka = [k] * 6
    metka[src] = 0
    visited = [False] * 6
    visited[src] = True
    predecessors = [-1] * 6  # Oldingilarni -1 bilan ishga tushiring, bu avvalgisi yo'qligini bildiradi
    for _ in range(6):
        q = minMetka(metka, visited)
        for c in range(6):
            if g[q][c] < k and not visited[c] and metka[q] + g[q][c] < metka[c]:
                metka[c] = metka[q] + g[q][c]
                predecessors[c] = q  # Update predecessor
        visited[q] = True

    for j in range(6):
        path = []
        if j != src:
            destination = j
            while destination != -1:
                path.append(destination + 1)  # 0-indekslangandan 1-indekslanganga aylantirish uchun 1 qo'shing
                destination = predecessors[destination]
            path.append(src + 1)  # Yo'lga manba tugunini qo'shing
            path.reverse()  # Uni manbadan manzilga olib borish uchun yo'lni teskari aylantiring
            print("Shortest path from", src + 1, "to", j + 1, ":", end=' ')
            for node in path:
                print(node, "->", end=' ')
            print("Distance:", metka[j])

g = [
    [k, 7, 9, k, k, 14],
    [k, k, 10, 15, k, k],
    [k, k, k, 11, k, 2],
    [k, k, k, k, 6, k],
    [k, k, k, k, k, 9],
    [k, k, k, k, k, k]
]

print("DFS Traversal:")
DFS(g)

print("\nDijkstra's Algorithm:")
dijkstra(g, 1)








#
#
#
# import sys
#
# NO_PARENT = -1
#
#
# def dijkstra(adjacency_matrix, start_vertex):
#     n_vertices = len(adjacency_matrix[0])
#
#     # shortest_distances[i] will hold the
#     # shortest distance from start_vertex to i
#     shortest_distances = [sys.maxsize] * n_vertices
#
#     # added[i] will true if vertex i is
#     # included in shortest path tree
#     # or shortest distance from start_vertex to
#     # i is finalized
#     added = [False] * n_vertices
#
#     # Initialize all distances as
#     # INFINITE and added[] as false
#     for vertex_index in range(n_vertices):
#         shortest_distances[vertex_index] = sys.maxsize
#         added[vertex_index] = False
#
#     # Distance of source vertex from
#     # itself is always 0
#     shortest_distances[start_vertex] = 0
#
#     # Parent array to store shortest
#     # path tree
#     parents = [-1] * n_vertices
#
#     # The starting vertex does not
#     # have a parent
#     parents[start_vertex] = NO_PARENT
#
#     # Find shortest path for all
#     # vertices
#     for i in range(1, n_vertices):
#         # Pick the minimum distance vertex
#         # from the set of vertices not yet
#         # processed. nearest_vertex is
#         # always equal to start_vertex in
#         # first iteration.
#         nearest_vertex = -1
#         shortest_distance = sys.maxsize
#         for vertex_index in range(n_vertices):
#             if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
#                 nearest_vertex = vertex_index
#                 shortest_distance = shortest_distances[vertex_index]
#
#         # Mark the picked vertex as
#         # processed
#         added[nearest_vertex] = True
#
#         # Update dist value of the
#         # adjacent vertices of the
#         # picked vertex.
#         for vertex_index in range(n_vertices):
#             edge_distance = adjacency_matrix[nearest_vertex][vertex_index]
#
#             if edge_distance > 0 and shortest_distance + edge_distance < shortest_distances[vertex_index]:
#                 parents[vertex_index] = nearest_vertex
#                 shortest_distances[vertex_index] = shortest_distance + edge_distance
#
#     print_solution(start_vertex, shortest_distances, parents)
#
#
# # A utility function to print
# # the constructed distances
# # array and shortest paths
# def print_solution(start_vertex, distances, parents):
#     n_vertices = len(distances)
#     print("Vertex\t Distance\tPath")
#
#     for vertex_index in range(n_vertices):
#         if vertex_index != start_vertex:
#             print("\n", start_vertex, "->", vertex_index, "\t\t", distances[vertex_index], "\t\t", end="")
#             print_path(vertex_index, parents)
#
#
# # Function to print shortest path
# # from source to current_vertex
# # using parents array
# def print_path(current_vertex, parents):
#     # Base case : Source node has
#     # been processed
#     if current_vertex == NO_PARENT:
#         return
#     print_path(parents[current_vertex], parents)
#     print(current_vertex, end=" ")
#
#
# # Driver code
# if __name__ == '__main__':
#     adjacency_matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#                         [4, 0, 8, 0, 0, 0, 0, 11, 0],
#                         [0, 8, 0, 7, 0, 4, 0, 0, 2],
#                         [0, 0, 7, 0, 9, 14, 0, 0, 0],
#                         [0, 0, 0, 9, 0, 10, 0, 0, 0],
#                         [0, 0, 4, 14, 10, 0, 2, 0, 0],
#                         [0, 0, 0, 0, 0, 2, 0, 1, 6],
#                         [8, 11, 0, 0, 0, 0, 1, 0, 7],
#                         [0, 0, 2, 0, 0, 0, 6, 7, 0]]
#     dijkstra(adjacency_matrix, 0)

























