"""
Given two strings, write a method to decide if
one is a permutation of the other.

"""

# str_1= "google"
# str_2 = "ooggle"

str_1= "bad"
str_2 = "dab"

from itertools import permutations
permword = []


def allPermutations(str, str_2):
    # Get all permutations of string 'ABC'
    permList = permutations(str)
    for perm in list(permList):
        permstr = (''.join(perm))
        permword.append(permstr)
    if str_2 in permword:
        return "Is a permutation"
    else:
        return "Is not a permutation"



if __name__ == "__main__":
    str = 'ABC'
    ans = allPermutations(str_1, str_2)
    print(ans)

