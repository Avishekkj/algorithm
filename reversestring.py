"""
Given a string with a set of words separated by whitespace,
reverse the order of the words.
Example:
    Initial String:
    this is a string reversal problem
    Resulting String:
    problem reversal string a is this
"""

str = "this is a string reversal problem"
#str_2= []






def reversestring(str):
    str_2 = str.split(' ')
    for i in range(1, len(str_2) + 1):
        print (''.join(str_2[-i]), end=' ')


if __name__=="__main__":
    reversestring(str)










# if __name__ =="__main__":
#     print(reversestring(str))