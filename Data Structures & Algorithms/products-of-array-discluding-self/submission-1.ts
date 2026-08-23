class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        const n = nums.length
        let fwd = Array(n).fill(1)
        let bkwd = Array(n).fill(1)

        for (let i = 1; i < n; i++) {
            fwd[i] = fwd[i - 1] * nums[i - 1]
        }

        for( let i = n - 2; i >= 0; i--) {
            bkwd[i] = bkwd[i + 1] * nums[i + 1]
        }   

        const res = fwd.map((f, i) => {
            const b = bkwd[i]
            return f * b
        })

        return res
    }
}
