int removeDuplicates(int* nums, int numsSize) {
    int k = 0;
    int curr = -101;
    for (int i = 0; i < numsSize; i++) {
        if(nums[i] != curr) {
            curr = nums[i];
            nums[k++] = curr;
        }
    }
    return k;
}