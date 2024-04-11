export function productExceptSelf(nums: number[]): number[] {
    let n = nums.length;
    let answer = new Array(n);
  
    // Calculate left products
    answer[0] = 1;
    for (let i = 1; i < n; i++) {
        answer[i] = nums[i - 1] * answer[i - 1];
    }
  
    // Calculate right products in the same array
    let right = 1;
    for (let i = n - 1; i >= 0; i--) {
        answer[i] *= right;
        right *= nums[i];
    }
  
    return answer;
}