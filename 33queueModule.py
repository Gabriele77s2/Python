# queue
from Queue import Queue
question_queue = Queue()

for x in range(1,10):
    temp_dict = ('key', x)
    question_queue.put(temp_dict)

while(not question_queue.empty()):
    item = question_queue.get()
    print(str(item))
# ('key', 1)
# ('key', 2)
# ('key', 3)
# ('key', 4)
# ('key', 5)
# ('key', 6)
# ('key', 7)
# ('key', 8)
# ('key', 9)

# deque
from collections import deque
d = deque([1, 2, 3])
p = d.popleft() # p = 1, d = deque([2, 3])
d.appendleft(5) # d = deque([5, 2, 3])

# Creating empty deque:
dl = deque() # deque([]) creating empty deque
# Creating deque with some elements:
dl = deque([1, 2, 3, 4]) # deque([1, 2, 3, 4])
# Adding element to deque:
dl.append(5) # deque([1, 2, 3, 4, 5])
# Adding element left side of deque:
dl.appendleft(0) # deque([0, 1, 2, 3, 4, 5])
# Adding list of elements to deque:
dl.extend([6, 7]) # deque([0, 1, 2, 3, 4, 5, 6, 7])
# Adding list of elements to from the left side:
dl.extendleft([-2, -1]) # deque([-1, -2, 0, 1, 2, 3, 4, 5, 6, 7])
# Using .pop() element will naturally remove an item from the right side:
dl.pop() # 7 => deque([-1, -2, 0, 1, 2, 3, 4, 5, 6])
# Using .popleft() element to remove an item from the left side:
dl.popleft() # -1 deque([-2, 0, 1, 2, 3, 4, 5, 6])
# Remove element by its value:
dl.remove(1) # deque([-2, 0, 2, 3, 4, 5, 6])
# Reverse the order of the elements in deque:
dl.reverse() # deque([6, 5, 4, 3, 2, 0, -2])

# limit deque size
from collections import deque
d = deque(maxlen=3) # only holds 3 items
d.append(1) # deque([1])
d.append(2) # deque([1, 2])
d.append(3) # deque([1, 2, 3])
d.append(4) # deque([2, 3, 4]) (1 is removed because its maxlen is 3)

# Breadth First Search
from collections import deque
def bfs(graph, root):
    distances = {}
    distances[root] = 0
    q = deque([root])
    while q:
        # The oldest seen (but not yet visited) node will be the left most one.
        current = q.popleft()
        for neighbor in graph[current]:
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                # When we see a new node, we add it to the right side of the queue.
                q.append(neighbor)
    return distances

graph = {1:[2,3], 2:[4], 3:[4,5], 4:[3,5], 5:[]}
bfs(graph, 1)
# {1: 0, 2: 1, 3: 1, 4: 2, 5: 2}
bfs(graph, 3)
# {3: 0, 4: 1, 5: 1}
