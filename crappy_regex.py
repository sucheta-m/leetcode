class Solution:
    def processStar(self, prevp, prevs, currs: str):
        if prevp == ".":
            return True
        elif prevs == currs:
            pass

    def isMatch(self, s: str, p: str) -> bool:
        prevs = s[0]
        prevp = p[0]
        if len(p)>len(s):
            loop = len(p)
        else:
            loop = len(s)
        for i in range(loop):
            try:
                p[i]
            except IndexError:
                return False
            if p[i] == ".":
                prevs = s[i]
                prevp = p[i]
                continue
            elif p[i] == "*":
                resStar = self.processStar(prevp, prevs, s[i])
                prevs = s[i]
                prevp = p[i]
                if resStar == True:
                    return True

            else:
                if p[i] == s[i]:
                    prevs = s[i]
                    prevp = p[i]
                elif p[i] != s[i]:
                    return False
        return True
                
            
def main():
    sol = Solution()
    val = sol.isMatch("aa","a")
    print(val)

if __name__ == "__main__":
    main()  
                

        
