class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
            Understand: 
                array has n distinct numbers in range [0, n] 
                return the number in range that is not in array
            ex: [0, 1, 2, 5, 4] 3 is missing

            Match: 
                Set + Array 
            Plan: 
            init set

            iterate 0 to n and add each elem in set (inclusive) 
            iterate through array and if num is in set, remove from set 

            return elem in set
        ---
        O(n) solution
        '''
        numsSet = set() 
        
        for i in range(0, len(nums) + 1):
            numsSet.add(i)

        for i in nums:
            if i in numsSet:
                numsSet.remove(i)
        
        return numsSet.pop()
