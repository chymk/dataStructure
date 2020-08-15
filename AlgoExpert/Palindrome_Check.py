'''
Write a function that takes in a non-empty string and that returns a boolean representing
whether or not the string is a palindrome. A palindrome is dened as a
string that is written the same forward and backward.

Sample input:"abcdcba"

Sample output: True (it is a palindrome)
'''

def isPalindrome(str):
    palString = list(str)
    flag = True
    length = len(palString)-1
    for i in range(0,length):
        if palString[i] != palString[length-i]:
            flag = False
            return False
    return flag

str='abcdba'

print(isPalindrome(str))
