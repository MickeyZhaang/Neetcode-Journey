class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mappings = {}

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            
            string_key = str(key)

            if string_key not in mappings:
                mappings[string_key] = []
            mappings[string_key].append(s)
        
        return list(mappings.values())
