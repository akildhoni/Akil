a = [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
b = [ ]
c = { }
for i in a :
    if i not in b :
        if a.count(i)>1:
            c[i]=a.count(i)
print(c)
