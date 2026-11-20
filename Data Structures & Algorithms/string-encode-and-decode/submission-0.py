class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            result.append(s[i:i + length])
            i += length
        return result
