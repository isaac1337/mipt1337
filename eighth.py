a=set([int(i) for i in input().split()])
b=set([int(i) for i in input().split()])
def unique(x):
    x=len(x)
    return x
print(unique(a), unique(b))
print(unique(a.union(b)))
print(a.intersection(b))