export function productExceptSelf(nums: number[]): number[] {
    const left = [...nums].map((n, i, array) => {
        if (i === 0) {
            return array[0] = n;
        }
        return array[i] *= array[i-1];
    });
    const right = [...nums].reverse().map((n, i, array) => {
        if (i === 0) {
            return array[0] = n;
        }
        return array[i] *= array[i-1];
    });
    return left.map((_n, i, array) => {
        if (i === 0) {
            return right[right.length - 2];
        }
        if (i === left.length - 1) {
            return left[i-1];
        }
        const res = right[right.length - i-2] *  array[i-1];

        return res;
    });
};