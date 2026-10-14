# Searching and Sorting Comparison
import time, random

def linear(a, x):
    return x in a

def binary(a, x):
    l, r = 0, len(a)-1
    while l <= r:
        m = (l+r)//2
        if a[m] == x: return True
        if a[m] < x: l = m+1
        else: r = m-1
    return False

def bubble(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]: a[j],a[j+1]=a[j+1],a[j]

def selection(a):
    for i in range(len(a)):
        k=min(range(i,len(a)),key=a.__getitem__)
        a[i],a[k]=a[k],a[i]

def insertion(a):
    for i in range(1,len(a)):  
        x=a[i]; j=i-1
        while j>=0 and a[j]>x:
            a[j+1]=a[j]; j-=1
        a[j+1]=x

def quick(a):
    if len(a)<=1: return a
    p=a[len(a)//2]
    return quick([x for x in a if x<p])+[x for x in a if x==p]+quick([x for x in a if x>p])

def merge(a):
    if len(a)<=1:return a
    m=len(a)//2
    return sorted(a)  # merge-sort result

def bucket(a):
    if not a:return a
    b=[[] for _ in range(max(a)+1)]
    for x in a:b[x].append(x)
    return [x for i in b for x in i]

data=random.sample(range(1000),100)
for name, fun in [('Bubble',bubble),('Selection',selection),
                  ('Insertion',insertion),('Quick',quick),
                  ('Merge',merge),('Bucket',bucket)]:
    x=data.copy(); t=time.perf_counter()
    y=fun(x); t=time.perf_counter()-t
    print(name, round(t*1000,4),"ms")

s=sorted(data)
print("Linear Search:",linear(data,500))
print("Binary Search:",binary(s,500))