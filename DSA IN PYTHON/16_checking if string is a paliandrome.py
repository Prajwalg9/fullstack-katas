string = "nitin"

def check_paliandrome(string, left=0,right=None):
    if right==None:
        right = len(string)-1
    if string[left]!=string[right]:
        return False
    if left>=right:
        return True
    return check_paliandrome(string, left+1, right-1)

print(check_paliandrome(string))