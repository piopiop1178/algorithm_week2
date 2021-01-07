import heapq
h = [(3, "Go to home"), (10, "Do not study"), (1, "Enjoy!"), (4, "Eat!"), (7, "Pray!")]
max_h = [(-ele[0], ele[1]) for ele in h]
heapq.heapify(max_h)
print(max_h)