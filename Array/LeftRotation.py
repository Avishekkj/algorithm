
import math
import os
import random
import re
import sys



def rotLeft(a, d):
    l = len(a)
    # print(a[d:n])
    # print(a[0:d])
    # a[:] = a[d:n] + a[0:d]
    #
    # print(a)

    for i in range(d):
        temp = a[0]
        for n in range(l - 1):
            a[n] = a[n + 1]
        a[l - 1] = temp

    print(a)







if __name__ == '__main__':



    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))



    result = rotLeft(a, d)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
