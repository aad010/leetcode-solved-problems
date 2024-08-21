class NumArray:
    '''
    Understand:
    1,2,3,4,5 
    2 4 7 11 16
    if left = 0 and right = 3, we return (11 - 2) + 2 = 11
    if left = 1 and right = 3, we return 11 - 2 = 9

    Match: Prefix Sum!

    Pseudocode:
        sumRange function: 
        
        init array to store prefix sums (prefixSum)

        using that prefix sum get sum btwn left and right indices
        if left index = 0 then return (prefixSum[right] - prefixSum[left]) + prefixSum[left]
        else return prefixSum[right] - prefixSum[left - 1]

    '''

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        prefixSum = []
        prefixSum.append(self.nums[0])

        for i in range(1, len(self.nums)):
            prefixSum.append(prefixSum[i - 1] + self.nums[i])
        
        if left == 0: 
            return (prefixSum[right] - prefixSum[left]) + prefixSum[left]
        else: 
            return (prefixSum[right] - prefixSum[left - 1])
        
            
