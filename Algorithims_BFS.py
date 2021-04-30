"""
BFS - Breadth First Search
From the root node we Search through nodes at that height before advancing deeper into the tree (sides)
Uses a Queue to explore its nodes, FIFO

1. Start by putting any one of the graph's verticies toward the back of the queue
2. Move our front item of the queue to the visited list
3. Create a list of vertex's adjacent nodes an add those to which are not within the visited list to the rear of the
queue
4.Repeat 2 & 3 untill queue is empty
"""

exGraph = {"5": ["3","7"],
          "3": ["2","4"],
          "7": ["8"],
          "2": [],
          "4": ["8"],
          "8": []}


visited = [] # Track visited nodes
queue = [] # Initialize queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(visited,exGraph,"5")
