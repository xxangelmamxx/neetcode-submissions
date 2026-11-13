class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_chars = ["".join(sorted(s)) for s in strs]
        temp = {}

        for i in range(len(strs)):
            temp.setdefault(sorted_chars[i], []).append(strs[i])
        
        fin = list(temp.values())

        return fin