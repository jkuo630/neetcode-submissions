class Solution:

    def encode(self, strs: List[str]) -> str:
        output_string = ""
        for string in strs:
            output_string += str(len(string))
            output_string += "#"
            output_string += string
        return output_string 

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

    # Input: ["neet","code","love","you"]
    # Output ["4#neet4#code4#love3#you]
    # Output ["neet","code","love","you"]
