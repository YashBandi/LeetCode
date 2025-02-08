class NumberContainers:
    def __init__(self):
        self.m = {}
        self.d = {}
    def change(self, i, n):
        if i in self.m and self.m[i]==n: return
        self.m[i] = n
        self.d.setdefault(n, [])
        heapq.heappush(self.d[n], i)
    def find(self, n):
        if n not in self.d: return -1
        while self.d[n] and self.m.get(self.d[n][0])!=n:
            heapq.heappop(self.d[n])
        return self.d[n][0] if self.d[n] else -1


    # Solution 2 (Time Limit Exceeded)

    # def __init__(self):
    #     self.index_map = {}  # Maps index -> number
    #     self.number_map = {}  # Maps number -> min-heap of indices

    # def change(self, index: int, number: int) -> None:
    #     # If index already exists, remove it from the old number heap
    #     if index in self.index_map:
    #         old_number = self.index_map[index]
    #         if old_number in self.number_map:
    #             self.number_map[old_number].discard(index)  # Lazy removal

    #     # Update index_map
    #     self.index_map[index] = number
        
    #     # Add index to the heap of the new number
    #     if number not in self.number_map:
    #         self.number_map[number] = set()
    #     self.number_map[number].add(index)
    # def find(self, number: int) -> int:
    #      # If number is not present or has no valid indices, return -1
    #     if number not in self.number_map or not self.number_map[number]:
    #         return -1

    #     # Return the smallest index
    #     return min(self.number_map[number])

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)