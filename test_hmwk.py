from hmwk import *
def test_palindrome():
    assert palindrome("Alen") == False
    assert palindrome("malayalam") == True
    assert palindrome("angel") == False
    assert palindrome("madam") == True
test_palindrome()


def test_tables():
    no9 = []
    no4 = []
    for i in range(1, 11):
         no9.append(9*i)
         no4.append(4*i)
         
    assert tables(9) == no9
    assert tables(4) == no4

def test_fizzbizz():
    list_values = [1, 2, 'fizz', 4, 'bizz', 'fizz', 7, 8, 'fizz', 'bizz', 11, 'fizz', 13, 14, 'fizzbizz', 16, 17, 'fizz', 19, 'bizz', 'fizz', 22, 23, 'fizz', 'bizz', 26, 'fizz', 28, 29, 'fizzbizz', 31, 32, 'fizz', 34, 'bizz', 'fizz', 37, 38, 'fizz', 'bizz', 41, 'fizz', 43, 44, 'fizzbizz', 46, 47, 'fizz', 49, 'bizz', 'fizz', 52, 53, 'fizz', 'bizz', 56, 'fizz', 58, 59, 'fizzbizz', 61, 62, 'fizz', 64, 'bizz', 'fizz', 67, 68, 'fizz', 'bizz', 71, 'fizz', 73, 74, 'fizzbizz', 76, 77, 'fizz', 79, 'bizz', 'fizz', 82, 83, 'fizz', 'bizz', 86, 'fizz', 88, 89, 'fizzbizz', 91, 92, 'fizz', 94, 'bizz', 'fizz', 97, 98, 'fizz', 'bizz']
    assert fizzbizz() == list_values

def test_panagram():
    all_letters = "sphinx of black quartz, judge my vow"
    rand = "alen"
    assert panagram(all_letters) == True
    assert panagram(rand) == False

def test_prime():
    till50 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    till10 = [2, 3, 5, 7]
    assert prime(50) == till50
    assert prime(10) == till10

def test_frequency():
    dict_sea = { ' ': 7,'a': 2, 's': 8, 'r': 1, 'e': 7, 't': 1, 'h': 4, 'l': 4, 'o': 2, 'n': 1}
    sea = "she sells sea shells on the sea shore"
    greeting = "helloalenhowareyou"
    dict_greeting = {'h':2,'e':3,'l':3,'o':3,'a':2,'n':1,'w':1,'r':1,'y':1,'u':1}
    assert frequency(sea) == dict_sea
    assert frequency(greeting) == dict_greeting
