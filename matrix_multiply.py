def mat(m,n):
    x=[]
    for i in range (m):
        y=[]
        for j in range (n):
            y.append(int(input()))
        x.append(y)
    return x 

print("enter element matrix A")
i=int(input("row"))
j=int(input("col"))
a=mat(i,j)
print(a)

print("enter element matrix B")
i=int(input("row"))
j=int(input("col"))
b=mat(i,j)
print(b)

result = [[0,0,0], [0,0,0], [0,0,0]] 
for i in range(len(a)): 
   for j in range(len(b)): 
      for k in range(len(b)): 
         result[i][j] += a[i][k] * b[k][j] 
print("The Resultant Matrix Is ::>")
for r in result: 
   print(r) 

