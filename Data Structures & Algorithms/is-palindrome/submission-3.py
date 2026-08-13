class Solution:
    def isPalindrome(self, s: str) -> bool:
        inp1 = s.lower()
        inp = ""
        for i in inp1:
            if ord(i) in range(ord('a'),ord('z')+1) or ord(i) in range(ord('0'),ord('9')+1):
                inp += i
        counter = 0
        for n in range(0,len(inp)//2):
            if inp[n] == inp[-(n+1)]:
                counter +=1
            else:
                return False
        if counter == len(inp)//2:
            return True
            return False
