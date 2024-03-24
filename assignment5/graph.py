from queue_array import *  # Needed for Breadth First Search

class Vertex:   # Add additional helper methods if necessary.
    def __init__(self, key):    # Add other attributes as necessary
        self.id = key
        self.adjacent_to = []   # list of other vertices the vertex is adjacent to
        self.visited = False    # helper attribute for determining connected components
        self.color = None   # helper attribute for bipartite graphs

    def __repr__(self):
        return "Vertex({!r})".format(self.id)

    def add_adjacent(self, vertex):  # helper function to add an adjacent vertex
        self.adjacent_to.append(vertex)

    def get_adjacent(self):  # helper function to get adjacent vertex
        return self.adjacent_to

    def set_color(self, col):   # helper function to set color
        self.color = col

    def get_color(self):   # helper function to get color
        return self.color

class Graph:    # Add additional helper methods if necessary.
    def __init__(self, filename):
        self.vertices = {}    # dictionary of vertices, {key: Vertex(key)}
        # reads in the specification of a graph and creates a graph using an adjacency list representation.
        with open(filename, "r") as filename:   # set up file to read
            lines = filename.readlines()
        for line in lines:  # create list of lines of the code
            key1 = "v" + line[0]  # v1, v2, etc.
            self.add_vertex(key1)
            if len(line) > 2:   # if vertex has an edge connection to other vertex
                key2 = "v" + line[2]
                self.add_vertex(key2)
                self.add_edge(key1, key2)   # each edge specified in the input file should appear on adjacency list

    def add_vertex(self, key):  # Add vertex to graph
        if key not in self.vertices:   # if vertex is already in graph
            self.vertices[key] = Vertex(key)

    def get_vertex(self, key):  # Return the Vertex object associated with the id.
        if key not in self.vertices:  # If id is not in the graph, return None
            return None
        return self.vertices[key]

    def add_edge(self, v1, v2):  # v1 and v2 are vertex id's. Assume that v1 and v2 are already in the graph
        self.vertices[v1].add_adjacent(v2)  # add an edge from v1 to v2
        self.vertices[v2].add_adjacent(v1)  # add an edge from v2 to v1

    def get_vertices(self):  # Returns a list of id's representing the vertices in the graph, in ascending order
        id_list = list(self.vertices.keys())
        no_v_list = [s.replace("v", "") for s in id_list]
        no_v_list.sort()
        return ["v" + id for id in no_v_list]

    def get_vertex_adjacent(self, key):  # helper function for getting adjacent vertex
        vertex = self.vertices[key]
        return vertex.get_adjacent()

    def conn_components(self):  # Returns a list of sublists in ascending order connected components
        v_list = self.get_vertices()    # initialize list of all vertices in ascending order
        connected_components = []   # initialize empty list of connected components
        counted = [False] * len(v_list)  # list for vertices not in a component graph yet
        for i in range(len(v_list)):
            if self.vertices[v_list[i]].visited is False:
                self.adjacent_helper(v_list[i])
                component = []
                for i in range(len(v_list)):
                    if self.vertices[v_list[i]].visited is True and counted[i] is False:
                        component.append(v_list[i])
                        counted[i] = True
                connected_components.append(component)
        self.set_visits_false()
        return connected_components  # get connected components using Depth First Search

    def adjacent_helper(self, key):  # helper function for connected components
        self.vertices[key].visited = True
        for i in self.get_vertex_adjacent(key):
            if self.vertices[i].visited is False:
                self.adjacent_helper(i)

    def set_visits_false(self):  # helper function: reset the visit boolean for all vertices in graph
        v_list = self.get_vertices()
        for i in v_list:
            self.vertices[i].visited = False

    def is_bipartite(self):  # Returns True if the graph is bicolorable and False otherwise.
        v_list = self.get_vertices()
        queue = Queue(len(self.vertices))   # make empty queue with capacity able to hold all vertices
        for i in range(len(v_list)):  # for loop through all vertices just to check
            if self.get_vertex_color(v_list[i]) is None:
                queue.enqueue(v_list[i])
                self.set_vertex_color(v_list[i], "black")  # set vertex color to black
                while queue.is_empty() is False:  # while there are items in queue (account for component graphs)
                    vertex = queue.dequeue()    # pop the vertex
                    color = self.get_vertex_color(vertex)  # color of popped vertex
                    for vert in self.get_vertex_adjacent(vertex):  # visit adjacent vertices
                        adj_color = self.get_vertex_color(vert)
                        if adj_color == color:   # same color as adjacent vertex color
                            return False
                        if adj_color is None:  # set color of adjacent vertex to opposite of popped vertex
                            if color == "black":
                                self.set_vertex_color(vert, "white")
                            else:
                                self.set_vertex_color(vert, "black")
                            queue.enqueue(vert)
        return True

    def set_vertex_color(self, key, color):  # helper function to set vertex color
        vertex = self.vertices[key]
        vertex.set_color(color)

    def get_vertex_color(self, key):    # helper function to get vertex color
        vertex = self.vertices[key]
        return vertex.get_color()
