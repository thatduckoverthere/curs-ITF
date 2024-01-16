n=int(input("Cate elemente sunt? "))

a=[]

for i in range(0,n):
    element=int(input("Introdu un element: "))
    a.append(element)

avg=sum(a)/n
print(f"Average of elements in the list{avg}")