class Element:
    def __init__(self,num,next=None):
        self.num=num
        self.next=next

class Spisok:
    def __init__(self):
        self.start=None
        self.end=None
        self.kol=0

    def add(self,elem):
        if (self.start==None):
            self.start=self.end=Element(elem,None)
        else:
            self.end.next=self.end=Element(elem,None)
        self.kol+=1

    def printsp(self):
        if (self.kol==0):
            print("No elements")
            return
        print("Your elements(",self.kol,") :")
        buf=self.start
        line=str(buf.num)+' '
        while(buf.next!=None):
            buf=buf.next
            line+=str(buf.num)
            line+=' '
        print(line)



def putnum(num):
    L=Spisok()
    while(num>0):
        elem=num%10
        L.add(elem)
        num=int(num/10)
    return L


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
        L.add(sum)
        L1.start=L1.start.next
        L2.start=L2.start.next
    if (q==1):
       while(L2.start!=None):
            L.add(L2.start.num+F)
            F=0
            L2.start=L2.start.next
    else:
        k=L1.kol-L2.kol
        while(L1.start!=None):
            L.add(L1.start.num+F)
            F=0
            L1.start=L1.start.next
    return L
        
    


print("Сложение чисел в виде списков.")
n1=int(input("Введите первое число:"))
L1=putnum(n1)
n2=int(input("Введите второе число:"))
L2=putnum(n2)
L1.printsp()
L2.printsp()
L=sum(L1,L2)
print("Результат:")
L.printsp()


