function highestValuePalindrome(s, n, k) {
    let arr = s.split('');
    const half = Math.floor(n / 2);
    let changesNeeded = 0;
    let changes = new Array(n).fill(false);  // Track changes for each position

    // First pass: Make the string a palindrome
    for (let i = 0; i < half; i++) {
        if (arr[i] !== arr[n - 1 - i]) {
            changesNeeded++;
            changes[i] = true;  // Mark index as changed
            // Set both characters to the maximum of the two
            arr[i] = arr[n - 1 - i] = Math.max(arr[i], arr[n - 1 - i]).toString();
        }
    }

    // If the required changes exceed the allowed, return -1
    if (changesNeeded > k) {
        return '-1';
    }

    let remainingChanges = k - changesNeeded;

    // Second pass: Maximize the palindrome
    for (let i = 0; i < half; i++) {
        // If already the maximum or no changes left, continue
        if (arr[i] === '9' || remainingChanges <= 0) {
            continue;
        }

        // If this position was changed, we can make it '9' for free
        if (changes[i]) {
            if (arr[i] !== '9') {
                arr[i] = arr[n - 1 - i] = '9';
                remainingChanges--;  // Use one change since we're optimizing an already changed pair
            }
        } else {
            // We need two changes to make both sides '9'
            if (remainingChanges >= 2) {
                arr[i] = arr[n - 1 - i] = '9';
                remainingChanges -= 2;
            }
        }
    }

    // Handle the middle character for odd-length strings
    if (n % 2 === 1 && remainingChanges > 0 && arr[half] !== '9') {
        arr[half] = '9';
    }

    return arr.join('');
}