def rearrange_list(lst):
    lenth = len(lst)
    evenlist =[] 
    oddlist=[]
    for i in range(lenth):
        if lst[i] % 2 == 0:
            evenlist.append(lst[i])
        else:
            oddlist.append(lst[i])
    finallist=evenlist+oddlist
    return (finallist)
lst = [1,2,3,4,5,6,7,8,9]
new = rearrange_list(lst)
print(new)

