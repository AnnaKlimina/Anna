def sum(L1,L2):
    L=Spisok()
    k=L1.kol
    q=1
    F=0
    if(L1.kol>L2.kol):
        k=L2.kol
        q=2
    while(k>0):
        k-=1
        sum=L1.start.num+L2.start.num
        if (F==1):
            sum+=1
        if (sum>9):
            F=1
            sum-=10
        else:
            F=0
        L.addend(sum)
        L1.start=L1.start.next
        L2.start=L2.start.next
    if (q==1):
       while(L2.start!=None):
            L.addend(L2.start.num+F)
            F=0
            L2.start=L2.start.next
    else:
        k=L1.kol-L2.kol
        while(L1.start!=None):
            L.addend(L1.start.num+F)
            F=0
            L1.start=L1.start.next
    return L

from DZ1task1 import Element,Spisok,putnum

print("Сложение чисел в виде списков.")
n1=input("Введите первое число:")
L1=putnum(n1)
n2=input("Введите второе число:")
L2=putnum(n2)
L1.printsp()
L2.printsp()
L=sum(L1,L2)
print("Результат:")
L.printsp()
