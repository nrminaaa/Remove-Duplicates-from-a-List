def remove_duplicate(a):
    h=[]
    for i in a:
        if i not in h:
            h.append(i)
    return h
a=[1,2,1,3,3,4,4,5]
print(remove_duplicate(a))
