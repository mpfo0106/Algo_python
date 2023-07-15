# # 상하우 가 다 다른 색이면 끝.
# import sys
# from collections import deque
#
# # art = []
# # for i in range(n):
# #     pixes = sys.stdin.readline().strip()
# #     row = []
# #     for pix in pixes:
# #         row.append(pix)
# #     art.append(row)
# #
# # for row in art:
# #     for item in row:
# #         if item
# n = int(sys.stdin.readline().strip())
# graph = [[] for _ in range(n+1)]
# for _ in range()
#
# def bfs(graph, start, goal):
#     queue = deque()  # Create a queue for BFS
#     visited = set()  # Set to keep track of visited nodes
#     # Add the start node to the queue and mark it as visited
#     queue.append(start)
#     visited.add(start)
#
#     while queue:
#         node = queue.popleft()  # Retrieve the next node from the queue
#         if node == goal:
#             # Goal node found, return the path
#             return ...
#
#         # Process the neighbors of the current node
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 queue.append(neighbor)  # Add unvisited neighbor to the queue
#                 visited.add(neighbor)  # Mark neighbor as visited
#
#     # If the goal node is not found, return failure or None
#     return ...
#
#
# # Example usage:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
# start_node = 'A'
# goal_node = 'F'
# result = bfs(graph, start_node, goal_node)
# print(result)
