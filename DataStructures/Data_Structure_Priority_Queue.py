# Scenerio: Track the least played song in a playlist. The easiest solution is to sort the list but that is time
# time consuming, You only need to keep track of the song with the least hits by using a min heap or priorty queue

# Heaps are binary trees where every parent node has a value less than or equal to any of its children.
# Basically, this type of queue keeps track of the minimum value at all times. Thus, Position 0 in the queue holds
# the minimum value.

#PLEASE NOTE: Priority queues don't sort lists in ascending order. It just keeps the smallest element in the 0th
# position. The rest of the elements may or may not be sorted.

# 0. import heapq

# 1. heapify() - This operation enables you to convert a regular list to a heap. On peforming this operation the,
# smallest element is pushed to the 0th postion

# 2. heapq.heapify - convert a regular list to a heap, smallest number is pushed to position 0.

# 3. heapq.heappush(heap, item) - push an ITEM into the HEAP (heap is the actual name of the heap)

# 4. heapq.heappop(heap) - this operation returns the smallest element and pops it from the heap

# 5. heapq.heappushpop(heap, item) - adds an item, and pushes the smallest element. If you were to pushpop a value that
# is already the smallest element then it would be popped instead of what is already in the heap.

# 6. heapq.heapreplace(heap, item) - adds and replaces the smallest element but solves #5

print("Implementing a Priority queue.")
import heapq

list = [2,3,4,5,7,9,34,5,6,8,2,0]
print(f"List: {list}")

heapq.heapify(list)
print(f"heap: {list}")

heapq.heappush(list, 3)
print(f"heappush: {list}")

heapq.heappop(list)
print(f"heappop: {list}")

heapq.heappushpop(list, 0)
print(f"heappushpop: {list}")  # as you can see 0 wasn't added to the list because it became the smallest element.

heapq.heapreplace(list, 0)
print(f"heapreplace: {list}")  # the smallest element in the heap 2 is replaced by 0
