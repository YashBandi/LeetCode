class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        n = right + 1
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        # Implementing the sieve
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        # Collecting all primes in the range [left, right]
        primes = [i for i in range(left, right + 1) if is_prime[i]]
        
        # If there are less than two primes, return an empty list
        if len(primes) < 2:
            return [-1, -1]

        # Finding the closest pair of primes
        min_diff = float('inf')
        closest_pair = []

        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes[i - 1], primes[i]]
            if min_diff == 1: break

        return closest_pair
        
        # prime_num = []
        # composites = []
        # for i in range(2, right + 1):
        #     for j in range(2, right + 1):
        #             composites.append(i*j)
        # for i in range(2, right + 1):
        #     if i not in composites:
        #         prime_num.append(i)
       