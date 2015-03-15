def palindrome(var):
    length = len(var)
    tmp = ""
#    tmp = var
    for i in range(length-1, -1, -1):
     #       print "%s" % var[i]
            tmp += var[i]
                
    #print var
    #print tmp
    if (tmp == var):
       # print "True"
        return True
    else:
        #print"False"
        return False
