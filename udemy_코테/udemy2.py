# # 가장 많이 방문한 페이지를 몇번 방문했는지
# # 뒤로 b 앞으로 f
# # isdigit()
# # 현재 위치를 가지고 있을 포인터로 옮기면서
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def solution(s):
    head = Node(None)  # Head node
    current = head
    visit = {}

    for item in s.split():
        if item.isdigit():
            # Create a new node for every visit
            new_page = Node(item)
            new_page.prev = current
            current.next = new_page
            current = new_page

            # Update visit count
            visit[item] = visit.get(item, 0) + 1

        elif item == 'B' and current.prev and current.prev.data is not None:
            # Move back if possible, ignoring if it's the head node
            current = current.prev
            visit[current.data] = visit.get(current.data, 0) + 1

        elif item == 'F' and current.next:
            # Move forward if possible
            current = current.next
            visit[current.data] = visit.get(current.data, 0) + 1
        # Else, ignore if 'B' or 'F' cannot be executed

    answer = max(visit.values(), default=0)
    return answer
#s ="1 2 3 4 B B 42 B F F"
s = "1 10 B B 20 1 F B B"
print(solution(s))  # Expected output: 4



#
# def most_visited_page(history):
#     # Splitting the input string into commands
#     commands = history.split()
#
#     # Stack to maintain the history of visited pages
#     page_stack = []
#     # Stack to maintain pages for forward command
#     forward_stack = []
#     # Dictionary to count visits to each page
#     visit_count = {}
#
#     for command in commands:
#         if command == 'B' and page_stack:
#             # Move back if possible and count the visit
#             forward_stack.append(page_stack.pop())
#             if page_stack:
#                 visit_count[page_stack[-1]] = visit_count.get(page_stack[-1], 0) + 1
#         elif command == 'F' and forward_stack:
#             # Move forward if possible and count the visit
#             page_stack.append(forward_stack.pop())
#             visit_count[page_stack[-1]] = visit_count.get(page_stack[-1], 0) + 1
#         else:
#             # Visit a new page
#             page = command
#             page_stack.append(page)
#             forward_stack.clear()  # Clear forward history as new page is visited
#             visit_count[page] = visit_count.get(page, 0) + 1
#
#     # Find the maximum number of visits
#     max_visits = max(visit_count.values(), default=0)
#
#     return max_visits
#
# # Example usage
# #history = "1 2 3 4 B B 42 B F F"
# history = "1 10 B B 20 1 F B B"
# print(most_visited_page(history))  # Should output 3

#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None
#
# def most_visited_page_linked_list(history):
#     # Splitting the input string into commands
#     commands = history.split()
#
#     # Initialize the dummy head node
#     head = Node(None)
#     current = head
#
#     # Dictionary to count visits to each page
#     visit_count = {}
#
#     for command in commands:
#         if command == 'B' and current.prev:
#             # Move back if possible
#             current = current.prev
#             if current.data is not None:  # Avoid counting dummy head node
#                 visit_count[current.data] = visit_count.get(current.data, 0) + 1
#
#         elif command == 'F' and current.next:
#             # Move forward if possible
#             current = current.next
#             if current.data is not None:
#                 visit_count[current.data] = visit_count.get(current.data, 0) + 1
#
#         elif command.isdigit():
#             # Create a new page node
#             new_page = Node(command)
#
#             # Remove forward links (if any)
#             current.next = new_page
#             new_page.prev = current
#
#             # Move to the new page
#             current = new_page
#
#             # Update visit count
#             visit_count[command] = visit_count.get(command, 0) + 1
#
#     # Find the maximum number of visits
#     max_visits = max(visit_count.values(), default=0)
#
#     return max_visits

# Example usage
# history = "1 10 B B 20 1 F B B"
# print(most_visited_page_linked_list(history))  # Expected output: 4
#
