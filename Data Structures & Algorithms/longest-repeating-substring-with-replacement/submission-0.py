class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window + dict for freq of chars in window 
        # keep increasing window as long as topfreqchar + k > total chars 

        freq = {}
        ans = 0 
        maxfreq = 0 
        left = 0 
        right = 0
        while right < len(s):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            maxfreq = max(maxfreq, freq[s[right]])

            while (maxfreq + k) < (right - left + 1):
                freq[s[left]] -= 1
                left += 1 
            
            ans = max(ans, right - left + 1)

            right += 1

        return ans
        
        