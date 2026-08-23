class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs: string[]): string {
        let res = ""
        for(const s of strs) {
            const len = s.length
            res += String(len) + "#" + s
        }
        return res
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str: string): string[] {
        let res = []
        let i = 0
        while (i < str.length) {
            let j = i;
            while(str[j] !== '#') {
                j++
            }
            let lenght = parseInt(str.substring(i, j))
            i = j + 1
            j = i + lenght
            res.push(str.substring(i, j))
            i = j
        }

        return res
    }
}
