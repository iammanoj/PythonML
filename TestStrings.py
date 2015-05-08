#!//Users/manoj_mohan/anaconda/bin/python

alist = 'abcdefghijklmnopqrstuvwxyz'
alist2 = ['klm','abc','bcde','rst','uvw','xyz']
print len(alist)
print len(alist2)

#print alist2
#print alist[1]

alist2.append('d')
alist2.sort()
"""
print alist2[:2]
print alist2[1:2]
print alist2[2:4]
"""
matrix= [(len(alist)/2),2] 
matrix = alist
#matrix[1][1] = 's'
#matrix = [[0 for i in xrange(5)] for i in xrange(5)]
"""
print matrix[1:5]
print matrix[2:9]
print matrix[2:11]
print matrix[1:13]
#print matrix[1,13]
"""
Str1 = raw_input('Enter a word to check against Dictionary :')
#if Str1 == '' :
#    print "String entered cannot be Empty!"
#    return false


char_cnt = 0
for char in Str1:
    if char.lower() in alist:
        char_cnt += 1
    else:
        break

if len(Str1) == char_cnt:
    print "All characters from the input word Exists!"
else:
    print "DOES NOT EXIST, False"

print alist

