class Solution():
    def convert(self, s, numRows):
        b = []
        max_index = len(s)-1
        
        m = 2*numRows-2
        k = 0 
        
        for i in range(numRows):
            j = 1 #count set
            k = i
            while (k <= max_index):
               b.append(s[k])
               if (m*j == 2*k):
                   j=j+1
                   k = m*j-k
                   j = j+1
               else:
                   k=m*j-k
                   j = j + 1
        return b
      
s = "PAYPALISHIRING"
A = Solution().convert(s, 3)
print ''.join(A)

