"""
   here I am creating a function that will build a graph from data.
   first, I imported the class Graph from classes.py because it has methods(like (add_edge))
   that are important when building a graph.
   Then I defined the function build_graph that will go through each triple (vertex1,vertex2,weight)
   one by one, add corresponding edge into a graph.
  finally, return a graph.
"""
from classes import Graph
# building a function that will read data and turn into a graph
def build_graph(triples):
   g = Graph()  # create empty graph

   for triple in triples :
       vertex1, vertex2, distance = triple
       try:
          g.add_edge(vertex1, vertex2, distance)
       except ValueError as e:
           print(f"Error:{e} and we have the same edge ({vertex1},{vertex2})")

   return g

