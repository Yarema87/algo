from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edges(self, edges):
        for u, v in edges:
            if u not in self.graph:
                self.graph[u] = {'color': None, 'neighbors': []}
            if v not in self.graph:
                self.graph[v] = {'color': None, 'neighbors': []}
            if v not in self.graph[u]['neighbors']:
                self.graph[u]['neighbors'].append(v)
            if u not in self.graph[v]['neighbors']:
                self.graph[v]['neighbors'].append(u)

    def get_neighbors(self, u):
        return self.graph[u]['neighbors']

    def get_node_color(self, u):
        return self.graph[u]['color']

    def set_node_color(self, u, color):
        self.graph[u]['color'] = color


def flood_fill(graph, start_node, new_color, visited=None):
    if visited is None:
        visited = set()

    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node in visited or graph.get_node_color(node) == new_color:
            continue

        original_color = graph.get_node_color(node)
        graph.set_node_color(node, new_color)
        visited.add(node)

        for neighbor in graph.get_neighbors(node):
            if graph.get_node_color(neighbor) == original_color and neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)


G = Graph()

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        characters = line.strip().split()
        for j, char in enumerate(characters):
            node_name = f"{chr(65 + i)}{j + 1}"
            G.graph[node_name] = {'color': char, 'neighbors': []}

num_rows = len(lines)
num_cols = len(lines[0].strip().split())
for i in range(num_rows):
    for j in range(num_cols):
        node_name = f"{chr(65 + i)}{j + 1}"
        if i > 0:
            G.add_edges([(node_name, f"{chr(65 + i - 1)}{j + 1}")])
        if i < num_rows - 1:
            G.add_edges([(node_name, f"{chr(65 + i + 1)}{j + 1}")])
        if j > 0:
            G.add_edges([(node_name, f"{chr(65 + i)}{j}")])
        if j < num_cols - 1:
            G.add_edges([(node_name, f"{chr(65 + i)}{j + 2}")])

start_node = 'A5'
new_color = 'P'

flood_fill(G, start_node, new_color)


with open('output.txt', 'w') as file:
    cols = len(lines[0].strip().split())
    for i, (node, attributes) in enumerate(G.graph.items(), 1):
        file.write(f"{attributes['color']} ")
        if i % cols == 0:
            file.write("\n")
