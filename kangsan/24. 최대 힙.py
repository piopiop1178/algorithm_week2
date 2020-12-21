import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
heap = [0]

def heappush(heap, n):
    heap.append(n)
    idx = len(heap) - 1
    parent = idx // 2

    while parent > 0:
        if heap[parent] < heap[idx]:
            heap[parent], heap[idx] = heap[idx], heap[parent]
            idx = parent
            parent = idx // 2
        else:
            break

def heappop(heap):
    if len(heap) > 1:
        heap[1], heap[-1] = heap[-1], heap[1]
        e = heap.pop()
        idx = 1

        while idx * 2 < len(heap):
            child = idx * 2
            
            if idx * 2 + 1 < len(heap):
                if heap[child] < heap[idx * 2 + 1]:
                    child = idx * 2 + 1
            
            if heap[idx] < heap[child]:
                heap[idx], heap[child] = heap[child], heap[idx]
                idx = child
            else:
                break
        return e
    else:
        return 0

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        print(heappop(heap))
    else:
        heappush(heap, x)

