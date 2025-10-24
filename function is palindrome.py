def is_palindrome(s) :
    """
    s is a string
    returns True if s is a palindrome, returns False otherwise
    """
    return s == s[::-1]

print(is_palindrome("awawa"))
print(is_palindrome("222"))
print(is_palindrome("abcdef"))