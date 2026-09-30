"""
    here I am creating a function that will read json files,
    first, I imported the json builtin module
    Then I imported the build_graph function from BuildGraph.py because it's the one that contains
    the logic to turn data into a graph. so instead of rewriting the code, I reused it here.
    Then I created another function  graph_from_jsn that will
    open the json file in read mode and convert it into a list then build the graph.
     finally return the graph.

"""
import json
from BuildGraph import build_graph
# creating a graph based on the json file
def graph_from_jsn (file):
    with open(file,"r") as json_file:
        triples = json.load(json_file)
    return build_graph(triples)
