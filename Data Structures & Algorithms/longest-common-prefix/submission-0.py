class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimal_word = min(strs)
        i = 0

        while i < len(strs) and minimal_word:
            if not strs[i].startswith(minimal_word):
                minimal_word = minimal_word[:-1]
            else:
                i += 1
        
        return minimal_word