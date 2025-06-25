1. Acess the value 200 from this nested tuple?
g=(10,20,(30,40,(100,200)),50)
print(g[2][2][0])

output:
200

2.Accessvthe value 70 fromthe nested structure?
h=(10,(20,30,(40,50,(60,70))),80)
print(h[1][2][2][1])

output:
70

3.convert j=(10,20,30,40,50) tuple data type to list datatype?
j=(10,20,30,40,50)
res=list(j)
print(res)
print(type(res))

output:
[10,20,30,40,50]
<class 'list'>

4.Find common elements between two tuples?
k=(1,2,3,4)
h=(3,4,5,6)
res=[]
for i in k:
    if i in h and i not in res:
        res.append(i)
print(res)    

output:
[3,4]