

str_1 = "lucidProgramming"
str_2 = "LucidProgramming"
str_3 = "luCidprogramming"



def uppercaseletter(word):
     for i in range(len(word)):
         if word[i].isupper():
             return word[i]
     return "no upper case letter found"


def findupperrecursive(word, idx):
     if word[idx].isupper():
         return word[idx]
     if idx == len(word)-1:
         return "no upper case letter found"
     return findupperrecursive(word, idx+1)

print(findupperrecursive(str_1,0))
print(findupperrecursive(str_2,0))
print(findupperrecursive(str_3,0))


