'''
A student is taking a cryptography class and has found anagrams to be very useful.
Two strings are anagrams of each other if the first string's letters can be rearranged to form the
second string. In other words, both strings must contain the same exact letters in the same exact frequency.
For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

The student decides on an encryption scheme that involves two large strings.
The encryption is dependent on the minimum number of character deletions required to make the two strings
anagrams. Determine this number.

Given two strings,  and , that may or may not be of the same length, determine the minimum
number of character deletions required to make  and  anagrams. Any characters can be deleted from
either of the strings.

Example
a = 'cde'
b='dcf,
Delete  from  and  from  so that the remaining strings are  and  which are anagrams.
This takes  character deletions.
'''
import math
import os
import random
import re
import sys
from collections import Counter

#Complete the makeAnagram function below.



def makeAnagram(a, b):
     count = 0
     for item in a:
         if item not in b:
             count +=1
     for item in b:
         if item not in a:
             count +=1

     if count == (len(a) + len(b)):
         return "Anagram cannot be made"
     else:
         return count





dict1=(Counter("crxzwscanmligyxyvym"))
dict2=(Counter("jxwtrhvujlmrpdoqbisbwhmgpmeoke"))
print(dict1.values())
print(dict2.values())

print(("jxwtrhvujlmrpdoqbisbwhmgpmeoke","crxzwscanmligyxyvym"))

dict1.subtract(dict2)
print(sum(abs(i) for i in dict1.values()))



if __name__ == '__main__':
    pass
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #a = input()

    #b = input()

    #res = makeAnagram(a, b)
    #print(res)

    #fptr.write(str(res) + '\n')

    #fptr.close()