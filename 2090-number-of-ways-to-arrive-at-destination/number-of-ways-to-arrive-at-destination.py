class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        ways = [0]*n
        ways[0] = 1
        time = [float('inf')]*n
        time[0] = 0
        min_heap = [(0, 0)]

        while min_heap:
            time1, src = heapq.heappop(min_heap) 
            for dst, time2 in graph[src]:
                if time1+time2 < time[dst]:
                    time[dst] = time1+time2
                    ways[dst] = ways[src]
                    heapq.heappush(min_heap, (time[dst], dst))
                elif time1+time2 == time[dst]:
                    ways[dst] += ways[src]

        if ways[n-1] == float('inf'): return -1
        return ways[n-1]% (pow(10, 9) + 7 )  