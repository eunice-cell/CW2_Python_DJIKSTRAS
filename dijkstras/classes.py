'''
  In this python file, I created two classes edge which stores the starting vertex ending vertex and weight between them.
   and class Graph represents the graph as an edge list, it has 6 methods
   first one is degree which returns the number of edges connected to a given vertex.
   second one is add_edge which adds new edge with a given weight.
   third one is list_vertices which returns all unique vertices in the graph and store them in a set.
   fourth one is is_adjacent which checks whether two vertices are connected together by same vetex.
   fifth one is neighbours which returns all neighbouring vertices connected to a given vertex.
   sixth one is dijkstra which uses priority queue to find shorted path.

'''

from dataclasses import dataclass
import heapq
# use dataclass to create the class Edge, because it is simple, it's just to store the data.
# each edge connects two vertices with a weight(of our choice).
@dataclass
class Edge:
    vertex1: str
    vertex2: str
    weight: float=2.0


# Graph is represented as a list of Edge objects
class Graph:
    def __init__(self):
        self.edges = []

    def degree(self, vertex):
        count = 0
        for edge in self.edges:
            if edge.vertex1 == vertex or edge.vertex2 == vertex:
                count += 1
        return count

# this method connects vertices with the edges and the weights
    def add_edge(self, vertex1, vertex2, distance=2.0):
        #prevent definition of edges with the same end
        if vertex1 == vertex2:
            raise ValueError("Edges you want to define have the same end ")
     #  prevent duplicate edges
        for edge in self.edges:
            if (edge.vertex1 == vertex1 and edge.vertex2 == vertex2) or \
               (edge.vertex1 == vertex2 and edge.vertex2 == vertex1) :
                raise ValueError("duplicates not allowed ")
        self.edges.append(Edge(vertex1, vertex2, distance))

#list all vertices because the algorithm must know all nodes
    def list_vertices(self):
        #use set because we don't want duplicates
        vertices = set()
        #use for loop to go through all edges collecting vertices
        for edge in self.edges:
            vertices.add(edge.vertex1)
            vertices.add(edge.vertex2)
        return list(vertices)

# see if two vertices are connected directly (adjacent )
    def is_adjacent(self,vertex1, vertex2):
        for edge in self.edges:
           if (edge.vertex1 == vertex1 and edge.vertex2 == vertex2) or \
              (edge.vertex1 == vertex2 and edge.vertex2 == vertex1):
              return True
           #if no connecting edge found
        return False

# finding all neighbours of a given vertex so the algorithm which city to go to next
    def neighbours(self, vertex):
        # this is where the neighbours would be saved
        neighbours = []
        #created a loop that will go through all the edges one by one checking if the current vertex is on the right side of the edge then will add the left side neighbour vice versa
        for edge in self.edges:
            if edge.vertex1 == vertex:
                neighbours.append(edge.vertex2)
            elif edge.vertex2 == vertex:
                neighbours.append(edge.vertex1)
        return neighbours

# the dijkstra function that will get the shortest path frm the starting and then end node each edge
    def dijkstra(self, start, end):
      #get every node in the graph
        vertices = self.list_vertices()
        #use hashtable as they let us update quickly and compare the shortest paths
      # store the distances and start with inf as we assume he next node is unreachable (not 0 why? bcs we don'tknow the shortest path yet if o we assume thall all are reachable for free)
        distances ={v:float('inf') for v in vertices}
      # keep the previously visited node it incase we wanna know how we reached that node
        previous = {v:None for v in vertices}
     # set the starting distance to 0 (the rest remains infinity)
        distances[start] = 0
      #create a heap with the format (distance,vertex)
      # heap bcs keeps smallest at the top
        heap = [(0, start)]
      # create a while loop that will keep processing until the end is reached
        while heap:
            #removes and return smallest element from the heap
            current_distance, current = heapq.heappop(heap)
            #this says if the value you had is larger than the current it updates ignores the first one.
            if current_distance > distances[current]:
                continue
            if current == end:
                break
            # we look at the nodes connected to our current vertice
            for neighbour in self.neighbours(current):
                weight = None
                for edge in self.edges:
                    # checks because a to b is same as b to a
                    if (edge.vertex1 == current and edge.vertex2 == neighbour) or \
                       (edge.vertex2 == current and edge.vertex1 == neighbour):
                        # get the distance between two vertices (required to compute new pathlength)
                        weight = edge.weight
                        break
                if weight is None :
                    continue
                    # save the distance of the current node + the weight of the new edge
                new_distance = distances[current] + weight
                #if we find a shorter past update
                if new_distance < distances[neighbour]:
                    #update the new better distance
                   distances[neighbour]= new_distance
                   # records how we reached that neighbour so we can construct the path later
                   previous[neighbour] = current
                   # adds new node to heap
                   heapq.heappush(heap, (new_distance, neighbour))
# start reconstructing the path
        #if end wasn't reached then there is no path
        if distances[end]== float('inf'):
            return[],float('inf')
      # empty list
        path = []
        # start reconstructing from the end
        current = end
      # loop until we reach the start
        while current is not None:
            # add node to the beginning
            path.insert(0,current)
            # move to previous node
            current = previous[current]
          #returns the shortest path
        return path,distances[end]






