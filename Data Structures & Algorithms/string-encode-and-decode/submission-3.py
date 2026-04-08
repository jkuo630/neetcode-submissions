class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for string in strs:
            ans += str(len(string)) + "#" + string
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            curr_string = s[j + 1 : j + 1 + length]
            ans.append(curr_string)
            i = j + 1 + length
        
        return ans

    
    # Input: ["neet","code","is","great"]
    # Output ["4#neet4#code4#2is5#great]
    # Output ["neet","code","is","great"]

