a=set([1,2,3,4])
b=set([1,5,3,7,10])
#print(type(a))
#print(a)
print(a.union(b))
print(a.intersection(b))
#print(min(a))
#print((max(b)+min(b))/2)
print(a.difference(b))
print(b.difference_update(a))
print(b)