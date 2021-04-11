


def bubblesort(data):
    temp = 0
    lendata = len(data)
    swapped = False

    for i in range(lendata):
        for j in range(0,lendata-1-i):
            if data[j]> data[j+1]:
                temp = data[j]
                data[j]=data[j+1]
                data[j+1]= temp
                swapped= True
        if swapped == False:
            break

    return data






if __name__ == "__main__":

    list =  [9,3,32,31,43,21,54,98,75,57]
    #list = [1,23,43]

    result = bubblesort(list)

    print(result)