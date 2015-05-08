#!/Users/manoj_mohan/anaconda/bin/python

Dictionary = ["cat", "rat", "mat", "sat", "rug", "bed", "mug", "torn", "worn", "dusk", "desk", "rusk", "musk", "rode","road", "toad","mouse", "pie","tie","my"]

token = raw_input('Enter a token string to search :')
#token = "mytie"

"""
print "length of token entered is %s" % (len(token))
print "token 1:0 is %s"% (token[1:0])
print "token 0:1 is %s"% (token[0:1])
print "token 1:1 is %s"% (token[1:1])
print "token 1:2 is %s"% (token[1:2])
print "token 1:3 is %s"% (token[1:3])
print "token 1:4 is %s"% (token[1:4])
"""

i=0
tokenCnt = 0
while i <= len(token):
    partToken = token[0:i]
    #print partToken
    if partToken in Dictionary:
        print "This token %s exists in Dictionary...", (partToken)
        tokenCnt=1

    if i>0:
        j = i
        while j <= len(token):
            partToken2 = token[i:j]
	    #print partToken2
            if partToken2 in Dictionary:
                print "This token2 %s exists in Dictionary...", (partToken2)
                tokenCnt=1
            j+=1
    i+=1
#print tokenCnt

if tokenCnt == 0:
    print "This token DOES NOT EXIST in Dictionary"
