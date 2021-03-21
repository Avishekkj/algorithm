s1 = "fairy tales"
s2 = "rail safety"
from collections import Counter
# s1 = "listen"
# s2 = "silent"

ht = dict()


def is_anagram(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1)!=len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i  in s2:
        if i in ht:
            ht[i] -=1
        else:
            ht[i] = -1
    for value in ht.values():

        if value !=0 :
            return "Not an anagram"
        else:
            return "Yes, an anagram"





print(is_anagram(s1,s2))


def anagramusingsorterd(s1,s2):
    if sorted(s1)== sorted(s2):
        return "Yes, this is anagram"
    else:
        return "Not an anagram"

print(anagramusingsorterd(s1,s2))


def anagramusingsorterd(s1,s2):
    if Counter(s1)==Counter(s2):
        if sorted(s1) == sorted(s2):
            return "Yes, this is anagram"
        else:
            return "Not an anagram"


print(anagramusingsorterd(s1, s2))


def anagram(s1,s2):
    s1= sorted(s1)
    s2 = sorted(s2)
    print(s1,s2)
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            return False
    else:
        return True



ans = anagram(s1,s2)

if ans:
    print("Yes")
else:
    print("No")

