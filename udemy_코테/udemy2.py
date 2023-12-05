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
print(solution(s))


