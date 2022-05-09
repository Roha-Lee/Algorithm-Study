/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
 var merge = function(nums1, m, nums2, n) {
    if(n === 0) return nums1;
    for(let i = 0; i < m; i += 1) {
        if (nums1[i] <= nums2[0]) continue;
        else {
            const temp = nums2[0];
            nums2[0] = nums1[i];
            nums1[i] = temp;
            for(let j = 0; j < n - 1; j += 1) {
                if(nums2[j] < nums2[j+1]) break;
                const temp2 = nums2[j];
                nums2[j] = nums2[j+1];
                nums2[j+1] = temp2;
            }
        }
    }
    for(let i = m; i < m + n; i += 1) {
        nums1[i] = nums2[i-m];
    }
};