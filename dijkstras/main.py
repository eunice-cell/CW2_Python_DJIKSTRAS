'''
    Here I'm creating the output, what the user is going to see, and I am trying to make it as
    interactive as possible. on line 41 at first I had:
    (if "A" in vertices and "z" in vertices:
    path, distance = g.dijkstra("A", "z"))
    but in the question it says "The method should take two strings representing vertices, and
    return the shortest path between those vertices and the length of that path"
    as we can see, it doesn't say from A to Z but between 2 vertices, so I made it possible through line 41-63 for the user to
    select the 2 vertices they want to find the distance and from there the program will get the shortest path and distance as required in the question.
'''


from BuildJson import graph_from_jsn

files = ["../JSON/graph_1.jsn",
         "../JSON/graph_2.jsn",
         "../JSON/graph_3.jsn",
         "../JSON/graph_4.jsn",
         "../JSON/graph_5.jsn",
         "../JSON/my_graph.jsn"]
#create the options so the user can choose which graph to view
print("There are 6 graphs : ")
# number them from 1
for i in range(len(files)):
    print(f"{i+1}.  Graph {i+1}")
#ask the user which one they want to view

selection = input("\nSelect Graph: ")
 # check if the answer is a number or if it's a negative number and 0 or if number is bigger than the number of files that we have

if not selection.isdigit() or int(selection) < 1 or int (selection)> len(files):
  print("your selection is invalid")
else:
    file = files[int(selection)-1]

    g = graph_from_jsn(file)
    vertices = g.list_vertices()

    print(f"\nGraph {selection}")

    print (f'\nvertices:')
    print(vertices)
    print("\nEdges:")
# joi the edges to align them in one line
    print(" , " .join (f"{edge.vertex1}->{edge.vertex2}:({edge.weight}) " for edge in g.edges))\

    print("\nDegrees:")

    print(" , ".join(f"{vertex}: {g.degree(vertex)}" for vertex in vertices))
    while True:

        start = input("\nEnter your start vertex (or 'exit' to exit) : ").strip()

        if start.lower() == 'exit':
            break

        end = input("\nEnter your end vertex : ").strip()

        if start not in vertices or end not in vertices:
            print("your start and end vertex are invalid")
            continue

        path, distance = g.dijkstra(start, end)

        if distance==float('inf'):
            print("paths are disconnected")
        else:
            print(f"\nShortest Path:{path}")
            print(f"\nDistance:{distance}")

