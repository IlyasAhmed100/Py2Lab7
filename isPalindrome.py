def main():
    print(isPalindrome("racecar"))
    print()
    print(isPalindrome("palindrome"))

def isPalindrome(s):
    length = len(s)
    if length <= 1:     # Base case
        return True
    elif s[0] == s[length - 1]:
        shorter = s[1 : length - 1]
        return isPalindrome(shorter)
    return False

main()



