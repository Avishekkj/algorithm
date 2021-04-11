

mylst = [1,2,3,4,5,6]

total = 9
# (3,6)(4,5)


def findpairs(list , total):
    for i in range(len(mylst)):
        for j in range(i+1,len(mylst)):
            if mylst[i]+mylst[j]==total:
                print(mylst[i],mylst[j])



findpairs(mylst,total)





