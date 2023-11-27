def binary(a,key):
    i=0
    j=len(a)-1
    while i<=j:
        mid=(i+j)//2
        if a[mid]==key:
            return mid
        elif a[mid]<key:
            i=mid+1
        else:
            j=mid-1
    return -1
a=[10,20,25,60,40,90,74,35]
print(a)
key=int(input("enter key"))
a=binary(a,key)
if a!=-1:
    print(key,"found",a+1)
else:
    print(key,"not found")
