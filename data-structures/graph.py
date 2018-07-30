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

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self.__graph
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                for p in extended_paths: 
                    paths.append(p)
        return paths

graph = { "A": ["B", "C"], "B": ["D", "E"], "C": ["A"], "D": ["B", 'E'], "E": ["B", "D"] }

g = Graph(graph)
print(g)

path = g.find_all_paths("A", "E")
print(path)