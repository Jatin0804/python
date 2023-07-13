class Solution:
    def meetThem(self, A, B, C):
        # code here
        count = 0
        for i in range(2,22,2):
            for j in range(2, 22, 2):
                if i == j:
                    count += 1

        return count

a=2
b=2
c=22
ob = Solution()
ans = ob.meetThem(a, b, c)
print(ans)        