from hmwk import *
def test_palindrome():
    assert palindrome("Alen") == False
    assert palindrome("malayalam") == True
    assert palindrome("angel") == False
    assert palindrome("madam") == True
test_palindrome()
