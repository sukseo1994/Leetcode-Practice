class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lst = input.split('\n')
        stck = [] 
        max_len = 0 

        for f in lst:
            print(stck)
            res = 0 
            cleaned = f
            if '\t' in f:
                res = f.count('\t') 
                cleaned = cleaned.lstrip('\t') 
            while stck and stck[-1][1] >= res:
                stck.pop()
            stck.append([cleaned, res])
            if '.' in f:

                max_len = max(max_len, len('/'.join([c for c, v in stck])))
        return max_len