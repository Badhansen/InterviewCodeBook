# Arrays & Hashing

### ------------------------------------------------------------------------
# Problem 1: https://leetcode.com/problems/contains-duplicate/
# @Author: Badhan Sen

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        entries = set(nums)
        return True if len(entries) < len(nums) else False
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False

'''
Here N = Number of elements
Time Complexity: O(N)
Space Complexity: O(N)
'''

### ------------------------------------------------------------------------
# Problem 2: https://leetcode.com/problems/valid-anagram/
# @Author: Badhan Sen

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            count_s[s[i]] = count_s[s[i]] + 1
            count_t[t[i]] = count_t[t[i]] + 1
        return count_s == count_t
    
'''
Time Complexity: O(N + M)
Space Complexity: O(N + M)
'''

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = Counter(s), Counter(t)
        return a == b
    
'''
Time Complexity: O(N + M)
Space Complexity: O(N + M)
'''

### ------------------------------------------------------------------------
# Problem 3: https://leetcode.com/problems/two-sum/
# @Author: Badhan Sen

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen: 
                return [i, seen[complement]]
            seen[n] = i
        return [0, 0]
    
'''
Time complexity: O(N)
Space complexity: O(N)
'''

### ------------------------------------------------------------------------
# Problem 4: https://leetcode.com/problems/group-anagrams/
# @Author: Badhan Sen

from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord('a')] += 1
            anagrams[tuple(counts)].append(word)
        return list(anagrams.values())  # Convert to list before returning
'''
Time complexity: O(N * K), where N is the length of strs, and K is the maximum length of a string in strs.
Counting each string is linear in the size of the string, and we count every string.
Space complexity: O(N * K), total information store in anagrams
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sword = ''.join(sorted(word))
            anagrams[sword].append(word)
        return anagrams.values()

'''
Time complexity: O(N * K log K), where N is the length of strs, and K is the maximum length of a string in strs.
The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(Klog⁡K) time.

Space complexity: O(N * K), total information store in anagrams

'''

### ------------------------------------------------------------------------
# Problem 5: https://leetcode.com/problems/top-k-frequent-elements/
# @Author: Badhan Sen

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, count in counts.items():
            buckets[count].append(key)
        results = [key for bucket in buckets for key in bucket]
        return results[-k:]
  
'''
Time complexity: O(N)
Space complexity: O(N)
'''

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        answer = list()
        for key, value in counts.items():
            heapq.heappush(answer, (value, key))
            if len(answer) > k:
                heapq.heappop(answer)
        
        return [item[1] for item in answer]

'''
Time complexity: O(N log K)
    Initializing the Counter object takes O(n) time, where n is the number of elements in the nums list.
    The main loop iterates over each key-value pair in the counts dictionary, which takes O(n) time.
    Within the loop, heappush and heappop operations each take O(log k) time, where k is the size of the heap (which is at most k).
    Therefore, the overall 
    time complexity of the code is O(n log k), where n is the number of elements in the nums list and k is the value of k.
Space complexity: O(N + K)
    The counts dictionary stores the counts of each element in nums, which requires O(n) space.
    The answer list stores at most k elements, which requires O(k) space.
    Therefore, the overall space complexity is O(n + k).
'''

### ------------------------------------------------------------------------
# Problem 6: https://leetcode.com/problems/encode-and-decode-strings/
# @Author: Badhan Sen

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

### ------------------------------------------------------------------------
# Problem 7: https://leetcode.com/problems/product-of-array-except-self/
# @Author: Badhan Sen

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
'''
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right, res = [1] * n, [1] * n, [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = left[i] * right[i]
        return res
'''
Time complexity: O(n)
Space complexity: O(n)
'''

### ------------------------------------------------------------------------
# Problem 8: https://leetcode.com/problems/longest-consecutive-sequence/
# @Author: Badhan Sen

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        for i, n in enumerate(nums):
            seen[n] = i
        res = 0
        for n in nums:
            if (n - 1) not in seen:
                curr = n
                seq = 1
                while (curr + 1) in seen:
                    curr += 1
                    seq += 1
                res = max(res, seq)
        return res
'''
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
'''
Time complexity: O(n)
Space complexity: O(n)
'''
    
# Two Pointers

### ------------------------------------------------------------------------
# Problem 9: https://leetcode.com/problems/valid-palindrome/
# @Author: Badhan Sen

class Solution:
    def isPalindrome(self, s: str) -> bool:
        line = ''
        for c in s:
            if c.isalpha() or c.isdigit():
                line += c.lower()
        print(line)
        return line == line[::-1]
    
'''
Time complexity: O(N)
Space complexity: O(N)
'''

### ------------------------------------------------------------------------
# Problem 10: https://leetcode.com/problems/3sum/
# @Author: Badhan Sen

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = n + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    result.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result
    
'''
Time complexity: O(n^2)
Space Complexity: In this example O(1), as the sort method sorts the list in place, meaning it doesn't create a new list. It modifies the original list.
But it may be from O(log⁡n) to O(n), depending on the implementation of the sorting algorithm. For the purpose of complexity analysis, we ignore the memory required for the output.
'''

### ------------------------------------------------------------------------
# Problem 11: https://leetcode.com/problems/container-with-most-water/
# @Author: Badhan Sen

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        answer = 0
        while l < r:
            answer = max(answer, min(height[l], height[r]) * (r - l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return answer
'''
Time complexity: O(n)
Space complexity: O(1)
'''

# Sliding Window

### ------------------------------------------------------------------------
# Problem 12: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# @Author: Badhan Sen

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, minimum = 0, float("inf")
        for price in prices:
            minimum = min(minimum, price)
            res = max(res, price - minimum)
        return res
'''
Time complexity: O(n)
Space complexity: O(1)
'''

### ------------------------------------------------------------------------
# Problem 13: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# @Author: Badhan Sen

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = [-1] * 256
        maxLen, start = 0, -1
        for i, c in enumerate(s):
            if dic[ord(c)] > start:
                start = dic[ord(c)]
            dic[ord(c)] = i
            maxLen = max(maxLen, i - start)
        return maxLen
'''
Time complexity: O(n)
Space complexity: O(1)
'''

### ------------------------------------------------------------------------
# Problem 14: https://leetcode.com/problems/longest-repeating-character-replacement/
# @Author: Badhan Sen
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left, ans, maxCount = 0, 1, 0
        for right in range(len(s)):
            count[s[right]] += 1
            maxCount = max(maxCount, count[s[right]])
            while (right - left + 1 - maxCount) > k:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
    
'''
Time complexity: O(n)
Space complexity: O(n)
'''

### ------------------------------------------------------------------------
# Problem 15: https://leetcode.com/problems/minimum-window-substring/
# @Author: Badhan Sen

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash = defaultdict(int)
        for c in t:
            hash[c] += 1
        n, m = len(s), len(t)
        start, end, maxLen, count = 0, 0, float("inf"), 0
        index = 0
        while end < n:
            if s[end] in hash:
                hash[s[end]] -= 1
                if hash[s[end]] >= 0:
                    count += 1
            while count == m:
                if end - start + 1 < maxLen:
                    maxLen = end - start + 1
                    index = start
                if s[start] in hash:
                    hash[s[start]] += 1
                    if hash[s[start]] > 0:
                        count -= 1
                start += 1
            end += 1
        return "" if maxLen == float('inf') else s[index:index+maxLen]

'''
n = len(s), m = len(t)
Time complexity: O(n + m)
Space complexity: O(m)
'''
