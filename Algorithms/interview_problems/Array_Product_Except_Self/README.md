# Problem Title

Product of Array Except Self

## Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## Examples

- **Example 1:**
  - Input: `nums = [1,2,3,4]`
  - Output: `[24,12,8,6]`

- **Example 2:**
  - Input: `nums = [-1,1,0,-3,3]`
  - Output: `[0,0,9,0,0]`

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

## Follow up

Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

## Difficulty

Medium

## Specific Constraints

- The algorithm must run in O(n) time complexity.
- The division operation cannot be used.

## Hints

- Think about how you can use the result of the product of all numbers to the left and right of each index without using division.

## Language Specific Notes

- Be mindful of potential integer overflow when implementing the solution in languages that do not automatically handle integer overflow.

## Initial Solution (first_solution.ts)

The initial idea proposed in `first_solution.ts` involves having two arrays, each computing the cumulative product from each side of the array. Then, for each element, these products are multiplied together, excluding the current element.

This solution meets the problem's constraints but does not optimize for space complexity as requested in the follow-up question.

## Optimized Solution (best_solution.ts)

Following the hint for memory optimization, the final solution in `best_solution.ts` achieves O(1) extra space complexity, aside from the output array. This is accomplished by first calculating the product of all elements to the left of each index directly in the output array. Then, the right products are calculated in reverse, updating the output array in place with the final product, thereby eliminating the need for separate arrays for left and right products.

## Solution Evolution

- The transition from the initial to the optimized solution highlights the iterative process in technical interviews, where solutions are refined based on feedback or additional constraints.
- This approach not only meets the original problem's requirements but also addresses the follow-up challenge, showcasing the ability to optimize solutions further.

## Time and Space Complexity

- **Initial Solution:**
  - Time Complexity: O(n)
  - Space Complexity: O(n), due to the use of additional arrays for left and right products.
- **Optimized Solution:**
  - Time Complexity: O(n)
  - Space Complexity: O(1), if not considering the space needed for the output array as part of the space complexity.
