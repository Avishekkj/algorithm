
str = "No lemon no melon"

def checkpalindrom(str):
    for i in range(1,len(str)+1):
        if str[i].lower() == str[-i:].lower() and str[i].isalpha():
            return "Yes, palindrome"
        else:
            return "Not A Parlindrom"


print(checkpalindrom(str))

rev = ''.join(reversed(str))

print(rev)

revstr = ""

for i in str:
    revstr = revstr + i

if (str==revstr):
    print("yes")
else:
    print("NO")












