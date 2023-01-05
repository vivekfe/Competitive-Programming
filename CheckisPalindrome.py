class Solution:
    def isPalindrome(self, x: int) -> bool:
        check_list=[]
        while x!=0:
            y=x%10
            check_list.append(y)
            x=x//10
        z=len(check_list)
        for i in range(0,len(check_list)):
            if check_list[i]==check_list[z-1-i]:
                pass
            else:
                return False
        return True
