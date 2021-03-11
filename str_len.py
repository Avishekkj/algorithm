

input_str = "LucidProgramming"

def countlen(word):
     if word == "":
         return 0
     else:
         return 1+ countlen(word[1:])


print(countlen(input_str))