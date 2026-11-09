class Solution:
    def reverseString(self, s: List[str]) -> None:
        n=len(s)
        temp=''
        for i in range(len(s)//2):
            temp=s[n-1-i]
            s[n-i-1]=s[i]
            s[i]=temp
            


        return s
