## Problem Title

Remove Duplicates from Sorted Array

## Description

Given a sorted integer array `nums` in non-decreasing order, modify the array in-place to remove all duplicates. Each unique element should appear only once, and the order of elements should be maintained. The function should return the number of unique elements `k`, and modify the array such that the first `k` elements of `nums` contain the unique elements in the order they were initially present.

## Difficulty

Easy.

## Estimated Completion Time

30 minutes for JR or SSR position.

## Examples

- **Example 1:**
  - Input: `nums = [1,1,2]`
  - Output: `2`, `nums = [1,2,_]`
  - Explanation: The function returns `k = 2`, with the first two elements of `nums` being `1` and `2` respectively. The remaining elements beyond `k` are not important (represented as underscores).

- **Example 2:**
  - Input: `nums = [0,0,1,1,1,2,2,3,3,4]`
  - Output: `5`, `nums = [0,1,2,3,4,_,_,_,_,_]`
  - Explanation: The function returns `k = 5`, with the first five elements of `nums` being `0`, `1`, `2`, `3`, and `4` respectively. The remaining elements beyond `k` are not important (represented as underscores).

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

## Follow up

The task must be completed with an in-place algorithm, which means no extra space for another array, though a few extra variables are allowed.

## Solution Discussion

The solution involves using two pointers within the array to efficiently overwrite duplicate values with new unique elements found later in the array. This process involves:
- Iterating through each element of the array.
- Comparing the current element with the last unique element stored.
- If the current element is different, it is written to the position of the last found unique element's next position.
- This continues until the end of the array is reached, and `k` unique elements are found.

The provided C implementation is straightforward, using a variable `curr` to track the last unique number and an index `k` to place unique numbers back into the array.

## Time and Space Complexity
Time Complexity: O(n), where n is the number of elements in the array nums. The array is traversed once.
Space Complexity: O(1), as the modification is done in place and no additional storage is used beyond temporary variables.