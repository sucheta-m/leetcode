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

    def checkMatch(self, currs, nexts, p):
        truth_table = ([False]*len(s))*len(p)
        
        for match in pattern:
            if "*" in match:
                currp = match.split(*)
            

    def isMatch(self, s: str, p: str) -> bool:
        pattern = self.findPattern(p)

        for i in range(len(s)):
            checkMatch(self, s[i], s[i+1], p)
            
        return True
