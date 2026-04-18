from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq = {}                        # {number: count}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        # Step 2: Sort items by frequency (value) in descending order
        # freq.items() gives list of tuples: [(num, count), ...]
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Take top k numbers
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result
