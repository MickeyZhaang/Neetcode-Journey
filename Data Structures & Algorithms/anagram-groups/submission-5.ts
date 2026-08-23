class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const map = new Map<string, string[]>()

        for(let word of strs) {
            const counts = Array(26).fill(0)
            for(let c of word) {
                const cCode = c.charCodeAt(0)
                const aCode = 'a'.charCodeAt(0)
                counts[cCode - aCode] += 1
            }
            const key = counts.join(',')
            if(!map[key]) {
                map[key] = []
            }
            map[key].push(word)
        }
        return Object.values(map)
    }
}
