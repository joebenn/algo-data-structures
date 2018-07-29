class Graph(object):

    def __init__(self, graph=None):
        if graph == None:
            graph = {}
        self.__graph = graph

    def add_node(self, node):
        if node not in self.__graph:
            self.__graph[node] = []

    def add_edge(self, edge):
        edge = set(edge)
        (node1, node2) = tuple(edge)
        if node1 in self.__graph:
            self.__graph[node1].append(node2)
        else:
            self.__graph[node1] = [node2]

    def nodes(self):
        return list(self.__graph.keys())
    
    def edges(self):
        edges = []
        for node in self.__graph:
            for neighbour in self.__graph[node]:
                if (neighbour, node) not in edges:
                    edges.append((node, neighbour))
        return edges
    
    def __str__(self):
        result = "Nodes: "
        for node in self.nodes():
            result += str(node) + " "
        result += "\nEdges: "
        for edge in self.edges():
            result += str(edge) + " "
        return result

    def find_path(self, start_node, end_node, path=None):
        if path == None:
            path = []
        graph = self.__graph
        path = path + [start_node]
        if start_node == end_node:
            return path
        if start_node not in graph:
            return None
        for node in graph[start_node]:
            if node not in path:
                extended_path = self.find_path(node, end_node, path)
                if extended_path: 
                    return extended_path
        return None

graph = { "A": ["B", "C"], "B": ["D", "E"], "C": ["A"], "D": ["B", 'E'], "E": ["B", "D"] }

g = Graph(graph)
print(g)

path = g.find_path("A", "E")
print(path)