"""
DFS - Depth First Search
Starting from the root we search the full depth of one branch before moving onto another
Going through a Maze to the dead end before going back,
We should use recurision to complete all the "neighbors" in a graph before

Steps:
1. Pick our starting node
2. Print and add it to our visited list
3. Create a list create a list that adjacent node of the vertix, add the ones that haven't been visited
4. Recursive repeat 2 & 3 until the stack is empty
"""


exGraph = {"5": ["3","7"],
          "3": ["2","4"],
          "7": ["8"],
          "2": [],
          "4": ["8"],
          "8": []}


visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)




dfs(visited,exGraph,"5")
