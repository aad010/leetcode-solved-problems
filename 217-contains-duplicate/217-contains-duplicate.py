class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
          Understand: 
            return true if any num in int array appears > 1 else return false 
          Match: 
            hashmap + iteration through array

          Plan:
            init set

            for num in nums 
                if num not in set then add to it
                else return true 

            return false 

        ---
        O(n) solution  
        '''
        duplicatesSet = set() 

        for num in nums:
            if num not in duplicatesSet:
                duplicatesSet.add(num)
            else:
                return True
        
        return False
