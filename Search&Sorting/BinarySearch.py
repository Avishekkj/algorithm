#from collections import Counter

def binarysearch(my_list,search_number):
    left_index=0
    right_index= len(my_list)-1
    mid_index=0
    listindex = []

    count = Counter.

    while left_index < right_index:
        mid_index= (left_index + right_index)//2
        if  my_list[mid_index] ==search_number:
            listindex.append(mid_index)
            # return listindex
        if  search_number >my_list[mid_index]:
            left_index = mid_index+1
        else:
            right_index= mid_index-1

    return listindex




if __name__ == "__main__":

    list =  [2,12,21,34,54,65,72,81,81,81,85]
    number = 81

    result = binarysearch(list, number)
    print(result)


