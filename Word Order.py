from collections import Counter


list = []
def countuniqueword(words):
    print(len(set(words)))

def countfrequncy(words):
    count = dict()
    for  item in  words:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1

    for values in count.values():
        print(values,end=' ')




if __name__ == '__main__':
    n = int(input(" Enter the number of  words"))
    for word in range(0,n):
        n = str(input(" Enter words"))
        list.append(n)

countuniqueword(list)
countfrequncy(list)
