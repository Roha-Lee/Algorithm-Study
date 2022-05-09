/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
 var merge = function(nums1, m, nums2, n) {
    let pos1 = m-1; 
    let pos2 = n-1;
    let pos = m+n-1;
    while(pos1 >= 0 && pos2 >= 0) {
        if (nums1[pos1] < nums2[pos2]) {
            nums1[pos] = nums2[pos2];
            pos2 -= 1;
        }
        else {
            nums1[pos] = nums1[pos1];
            pos1 -= 1;
        }
        pos -= 1;
    }
    while(pos2 >= 0) {
        nums1[pos] = nums2[pos2];
        pos2 -= 1;
        pos -= 1;
    }
};