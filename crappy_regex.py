import numpy as np

class Solution:
    def findPattern(self, p):
        pattern = []
        for i in range(len(p)):
            if p[i] == "*":
                continue
            elif i+1 < len(p) and p[i+1] == "*":
                pattern.append(p[i:i+2])
            else:
                pattern.append(p[i])
        return pattern

    def make_tt(self, s, pattern):
        tt = np.full((len(pattern), len(s)), False)
        for match in range(len(pattern)):
            for char in range(len(s)):
                print(char, match)
                print(pattern[match])
                print(s[char])
                if s[char] == pattern[match].replace("*",""):
                    tt[match][char] = True
                print(tt[match][char])
        return tt
    
    def traverse_tt(self, tt, pattern):
        num_row, num_col = np.shape(tt)
        for row in range(num_row):
            for col in range(num_col):
                if tt[row][col] == True:
                    

            
    def isMatch(self, s: str, p: str) -> bool:
        pattern = self.findPattern(p)
        tt = self.make_tt(s, pattern)
        print(tt)
        return True
    
def main():
    sol = Solution()
    sol.isMatch("aabba", "a*ab*a")

if __name__ == "__main__":
        main()
