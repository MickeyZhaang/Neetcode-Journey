class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for s in strs:
            keyed = [0] * 26

            for c in s:
                idx = ord('a') - ord(c)
                keyed[idx] += 1

            s_keyed = str(keyed)

            if s_keyed not in seen:
                seen[s_keyed] = []
            seen[s_keyed].append(s)
        
        return list(seen.values())

