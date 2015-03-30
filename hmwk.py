from collections import OrderedDict
def palindrome(var):
    length = len(var)
    tmp = ""
    for i in range(length-1, -1, -1):
            tmp += var[i]
                
    if (tmp == var):
        print "True"
        return True
    else:
        print "False"
        return False
##def palindrome(var):
#     return var==var[::-1]
def tables(num):
    list_tables = []
    for i in range(0, 10):
        list_tables.append((i+1)*num)
        print "{:2} x {:2} = {:2}".format(i+1, num, list_tables[i])
    return list_tables

def fizzbizz():
    fizz = []
    for i in range (1, 101):
        if ((i % 3) == 0 and (i % 5) == 0): #if(i%15)==0
            print "fizzbizz"
            fizz.append("fizzbizz")
        elif i % 5 == 0:
            print "bizz"
            fizz.append("bizz")
        elif i % 3 == 0:
            print "fizz"
            fizz.append("fizz")
        else:
            print i
            fizz.append(i)
    return fizz

def panagram(stng):
    count = 0
    chara = "abcdefghijklmnopqrstuvwxyz"
    stng = stng.lower()
    for i in chara:
        if i in stng:
            count = count + 1
    if count == 26:
        return True
    else:
        return False

def prime(num):
    limit = []
    prime = []
    composite = []
    for i in range (2, num+1):
        limit.append(i)

    for j in limit:
        if j not in composite:
            for k in range(j*2, num+1, j):
                composite.append(k)

    for i in limit:
        if i not in composite:
            prime.append(i)
    return prime

def frequency(char):
    dict_freq = {}
    dict_ordered = {}
    frq_list = []
    for i in char:
        if i not in dict_freq:
            dict_freq.update({i:1})
        else:
            dict_freq[i]+=1
    for k in dict_freq:
           print "%s :: %s" % ( k, dict_freq[k])

    return dict_freq
    

tables(4)
tables(9)
palindrome("alen")
palindrome("malayalam")
fizzbizz()
frequency("she sells sea shells on the sea shore")
