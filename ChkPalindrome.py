#!/Users/manoj_mohan/anaconda/bin/python
############################################
#       Program Name    :       Check Palindrome Words 
#       Description     :       This program helps determine any combination of words from a given list of words if they can be joined together to form a Palindrome.
#       Coder           :       Manoj Mohan
#       Create Date     :       05/11/2015
#       Mod Log         :
#
#
#
############################################
## Import libraries

from copy import deepcopy

list = ["bat","tab","cat","tar","rat", "ough", "stuff"]

for item in list:
    for RestEachItem in list:
        if item <> RestEachItem:
            if item == RestEachItem[::-1]:
                print item, RestEachItem 
                list.remove(item)


