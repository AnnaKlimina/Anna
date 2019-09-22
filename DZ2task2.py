s=input("Введите текст:\n")
s=s.split()
mas=set([])
f=0
k={}
while(s!=[]):
    i=len(s)
    for j in range(i):
        if (s[j] in mas):
            k[s[j]]+=1
        else:
            mas.add(s[j])
            k[s[j]]=1
    s=input()
    s=s.split()
i=0
f=2
for j in mas:
    if(k[j]>i):
        i=k[j]
        s=j
for j in mas:
    if(k[j]==i):
        f-=1
    
if f:
    print(s,i)
else:
    print("-")
    
        
            
        
