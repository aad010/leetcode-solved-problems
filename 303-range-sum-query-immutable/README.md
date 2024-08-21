# [303 - Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/description/) (Easy)
  
  
Given an integer array nums, handle multiple queries of the following type:  
  
1. Calculate the **sum** of the elements of nums between indices <code style="color : gray">left</code> and <code style="color : gray">right</code> **inclusive** where <code style="color : gray">left <= right</code>. 

Implement the <code style="color : gray">NumArray</code> class:  
  
* <code style="color : gray">NumArray(int[] nums)</code> Initializes the object with the integer array <code style="color : gray">nums</code>.
* <code style="color : gray">int sumRange(int left, int right)</code> Returns the **sum** of the elements of <code style="color : gray">nums></code> between indices <code style="color : gray">left</code> and <code style="color : gray">right</code> **inclusive** (i.e. <code style="color : gray">nums[left] + nums[left + 1] + ... + nums[right]</code>). 
   
  
**Example 1:**

  **Input**  
    &nbsp; ["NumArray", "sumRange", "sumRange", "sumRange"]  
    &nbsp; [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]  
  **Output**  
    &nbsp; [null, 1, -1, -3]

  **Explanation**   
    &nbsp; NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);  
    &nbsp; numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1  
    &nbsp; numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1  
    &nbsp; numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3  
 

**Constraints:**  
* <code style="color : gray">1 <= nums.length <= 104</code>
* <code style="color : gray">-105 <= nums[i] <= 105</code>
* <code style="color : gray">0 <= left <= right < nums.length</code>
* At most <code style="color : gray">10^4</code> calls will be made to <code style="color : gray">sumRange</code>.
