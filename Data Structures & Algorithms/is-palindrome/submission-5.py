#Neetcode Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ''
        for i in s:
            #check if alphanumeric
            if i.isalnum():
                check += i.lower() #convert all to lowercase
        if check == check[::-1]:#check palindrome
            return True
        return False
