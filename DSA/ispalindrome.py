# x = "working12"
# y = " !#%&?"
# print(x.isalnum())
# print(y.isalnum())

# Approach in psuedocode
# convert the input string to lower case (s.lower()) to make the comparison case insensitive
# use two pointers, l and r initialized at the beginning and at the end of the string, respectively (l = 0, r = len(s) - 1)
# set a while loop (while l < r)
# if the char in position l is not alphanumeric (s[l].isalnum()), move the pointer to the right (l += 1)
# if the char in position r is not alphanumeric (s[r].isalnum()), move the pointer to the left (r -= 1)
# if the both chars at l and r are alphanumeric and not equal (s[l] != s[r]), return False (not a palindrome)
# if both chars are alphanumeric and equal, move each pointers inward (l += 1, r -=1)
# if the loop completes without returning, the string is a palindrome and then return True from the function

class Palindrome:
    def is_palindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True