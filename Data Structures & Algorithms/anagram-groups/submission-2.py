class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord('a') - ord(c)] += 1
            stringed_key = str(key)
            if stringed_key not in res:
                res[stringed_key] = []
            res[stringed_key].append(s)
        
        return list(res.values())