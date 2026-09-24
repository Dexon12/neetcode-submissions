class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i in range(len(strs)):
            normalized_string = str(sorted(strs[i]))
            if normalized_string in seen:
                seen[normalized_string].append(strs[i])
            else:
                seen[normalized_string] = [strs[i]]

        
        return list(seen.values())
