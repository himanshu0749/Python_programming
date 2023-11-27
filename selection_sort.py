def selection(a):
    for i in range(len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min=j
        (a[i],a[min])=(a[min],a[i])

a=[10,80,40,60,20,45,65]

selection(a)
print(a)
