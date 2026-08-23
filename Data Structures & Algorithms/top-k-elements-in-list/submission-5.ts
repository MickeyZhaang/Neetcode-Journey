class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const counts = Array.from({length: nums.length + 1}, () => [])
        const map = new Map();

        for(const n of nums) {
            if(!map[n]) map[n] = 0
            map[n]++
        }

        for(const [k,v] of Object.entries(map)) {
            counts[v].push(k)
        }

        const topK = []

        for(let i = nums.length; i > 0; i--) {
            const entry = counts[i]
            if(!entry) {
                continue
            }
            for(const e of entry) {
                topK.push(Number(e))
                if(topK.length === k) {
                    return topK
                }
            }
        }

        return topK
    }
}
