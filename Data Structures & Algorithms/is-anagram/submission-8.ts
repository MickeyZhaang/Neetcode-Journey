class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) {
            return false;
        }
        const seen = Array(26).fill(0)

        for(let i = 0; i < s.length; i++) {
            seen[s[i].codePointAt(0) - 'a'.codePointAt(0)] += 1
            seen[t[i].codePointAt(0) - 'a'.codePointAt(0)] -= 1
        }
        console.log(seen)
        for (let e of seen) {
            if(e !== 0) {
                return false
            }
        }
        return true
    }
}
