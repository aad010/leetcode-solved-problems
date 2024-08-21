
# [268. Missing Number](https://leetcode.com/problems/missing-number/) (Easy)

Given an array <code style="color : name_color">nums</code> containing <code style="color : name_color">n</code> distinct numbers in the range <code style="color : name_color">[0,n]</code>, return *the only number in the range that is missing from the array.*


**Example 1:**  
&nbsp; **Input:** nums = [3,0,1]  
&nbsp; **Output:** 2  
&nbsp; **Explanation:** n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums. 

**Example 2:**  
&nbsp;**Input:** nums = [0,1]  
&nbsp;**Output:** 2  
&nbsp;**Explanation:** n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

**Example 3:**  
&nbsp;**Input:** nums = [9,6,4,2,3,5,7,0,1]
&nbsp;**Output:** 8
&nbsp;**Explanation:** n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

**Constraints:**
* <code style="color : name_color">n == nums.length</code>
* <code style="color : name_color">1 <= n <= 104</code>
* <code style="color : name_color">0 <= nums[i] <= n</code>
* All the numbers of <code style="color : name_color">nums</code> are **unique**.
