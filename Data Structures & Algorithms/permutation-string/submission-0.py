class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1 

        s2_freq = {}
        left = 0
        for right in range(len(s2)):
            # Add current character to window
            char = s2[right]
            s2_freq[char] = s2_freq.get(char, 0) + 1
            
            # If window is too big, remove the left-most character
            if (right - left + 1) > len(s1):
                left_char = s2[left]
                s2_freq[left_char] -= 1
                if s2_freq[left_char] == 0:
                    del s2_freq[left_char] # Critical for dictionary comparison
                left += 1
            
            # Compare maps
            if s1_freq == s2_freq:
                return True
                
        return False
            