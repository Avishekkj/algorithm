
"""
Given a string with a set of words separated by whitespace,
reverse each word of the sentence individually in the sentence itself.
Example:
Input : Split Reverse Join
Output : tilpS esreveR nioJ
"""

str = "Split Reverse Join"
str_2 = []
revstr= []

def reverseeachword(str):
    str_2 = str.split(' ')
    for i in range(0, len(str_2)):
        word = ''.join(reversed(str_2[i]))
        revstr.append(word)
    return ' '.join(revstr)







if __name__ == "__main__":
    print(reverseeachword(str))