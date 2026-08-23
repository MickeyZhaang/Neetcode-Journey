class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            key = str(key)
            if key not in seen:
                seen[key] = []
            seen[key].append(s)
        
        return [v for k, v in seen.items()]
