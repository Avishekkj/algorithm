from array import *

arr1 = array('i', [1,3,5,3,21,4])
arr2 = array('i', [])



# print(len(arr1))



# for item in arr1:
#     print(item, end=' ')

def accessarray(array, index):
    if index > len(array):
        return "Out of index"
    else:
        print(array[index])

# accessarray(arr1,7)

def searchInArray(array1,value):
    for item in array1:
        if item == value:
            return array1.index(value)
    return "Value do not exist"



# print(searchInArray(arr1,32))

arr1.remove(4)
print(arr1)
arr1.insert(0,5)
print(arr1)

