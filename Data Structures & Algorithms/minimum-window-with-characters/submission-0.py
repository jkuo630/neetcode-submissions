class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # brute force -> check every string 
        # optimal -> freq of both s and t 
        # as long as valid window, keep trying to shrink 

        freq_t = {}
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1 
        
        freq_window = {}
        left = 0 
        have = 0 
        need = len(freq_t) 
        ans = ""
        ans_len = float('inf')
        for right in range(len(s)):
            freq_window[s[right]] = freq_window.get(s[right], 0) + 1 
            if s[right] in freq_t and freq_window[s[right]] == freq_t[s[right]]:
                have += 1 
            
            while have == need:
                if (right - left + 1) < ans_len:
                    ans = s[left:right+1]
                    ans_len = right - left + 1
                freq_window[s[left]] -= 1 
                if s[left] in freq_t and freq_window[s[left]] < freq_t[s[left]]:
                    have -= 1 
                left += 1 
        
        return ans 