class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=s.lower()
        num = {'0','1','2','3','4','5','6','7','8','9'}
        k=''
        stat=False
        for i in t:
            if i in num or ord(i)<=122 and ord(i)>=97:
                k+=i
        if len(k)<=1:
            return True
        else:
            for i in range(len(k)//2):
                    stat=False
                    if k[i]==k[len(k)-i-1]:
                        stat=True
            return stat
        