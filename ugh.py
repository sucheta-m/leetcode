import numpy as np

class Solution:
    def __init__(self, string, pattern):
        self.s = string
        self.p = pattern
        self.pattern = []

    def findPattern(self):
        for i in range(len(self.p)):
            if self.p[i] == "*":
                continue
            elif i+1 < len(self.p) and self.p[i+1] == "*":
                self.pattern.append(self.p[i:i+2])
            else:
                self.pattern.append(self.p[i])
        return self.pattern

    def make_tt(self):
        self.tt = np.full((len(self.pattern), len(self.s)), False)
        for match in range(len(self.pattern)):
            for char in range(len(self.s)):
                if self.s[char] == self.pattern[match].replace("*",""):
                    self.tt[match][char] = True

    
    def check_bounds(self, row, col):
        if row == len(self.pattern) or col == len(self.s):
            return False

    def traverse_tt(self, row, col):
        valid = False
        if self.check_bounds(row, col) == False or self.tt[row][col] == False:
            return False
        if row == len(self.pattern) -1 and col == len(self.s)-1 and self.tt[row][col]:
            return True
        
        if "*" in self.pattern[row]:
            valid = valid or self.traverse_tt(row, col+1)
        valid = valid or self.traverse_tt(row+1, col+1)
        return valid
        

    def isMatch(self) -> bool:
        self.pattern = self.findPattern()
        self.make_tt()
    
def main():
    sol = Solution("aabba", "a*ab*a")
    sol.isMatch()
    print(sol.traverse_tt(0,0))

if __name__ == "__main__":
        main()
    

