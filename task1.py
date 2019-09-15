class Element:
    def __init__(self,num,next=None):
        self.num=num
        self.next=next

class Spisok:
    def __init__(self):
        self.start=None
        self.end=None
        self.kol=0

    def addend(self,elem):#добавление элемента в конец списка
        if (self.start==None):
            self.start=self.end=Element(elem,None)
        else:
            self.end.next=self.end=Element(elem,None)
        self.kol+=1

    def addstart(self,elem):#добавление элемента в начало списка
        if (self.start==None):
            self.start=self.end=Element(elem,None)
        else:
            buf=self.start
            self.start=Element(elem,None)
            self.start.next=buf
        self.kol+=1

    def addin(self,elem,pos):#добавление элемента в середину списка
        if (pos<0) or (pos>self.kol+1):
            print("Wrong position!\n")
            return 0
        if (pos==1):
            self.addstart(elem)
        else:
            if(pos==self.kol+1):
                self.addend(elem)
            else:
                buf=self.start
                buf2=Element(elem,None)
                while(pos>1):
                    buf=buf.next
                    pos-=1
                buf2.next=buf.next
                buf.next=buf2
                self.kol+=1
        return 1

    def delstart(self):#удаление первого элемента
        if (self.start!=None):
            self.start=self.start.next
            self.kol-=1
            return 1
        else:
            print("There are no elements!\n")
            return 0

    def delend(self):#удаление последнего элемента
        if (self.end!=None):
            k=self.kol
            buf=self.start
            while(k>2):
                k-=1
                buf=buf.next
            buf.next=None
            self.kol-=1
            return 1
        else:
            print("There are None elements!\n")
            return 0

    def delin(self,pos):#удаление элемента из середины списка
        if(self.start==None) or (pos<0) or (pos>self.kol):
            print("Wrong attributes!\n")
            return 0
        if(pos==1):
            self.delstart()
        else:
            if(pos==self.kol):
                self.delend()
            else:
                buf=self.start
                while(pos>2):
                    buf=buf.next
                    pos-=1
                buf.next=buf.next.next
                self.kol-=1
        return 1

    def info(self):
        print(self.kol,"elements.")

    def search(self,elem):
        buf=self.start
        k=0
        while(buf!=None):
            k+=1
            if(buf.num==elem):
                print("Element is found. its position is",k)
                return 
            buf=buf.next
        print("Element isn't found.")

    def find(self,pos):
        if(pos>self.kol) or (pos<1):
            print("Wrong position!")
        else:
            line="Element № "+str(pos)+" is "
            if (pos==1):
                line+=str(self.start.num)
            else:
                if (pos==self.kol):
                    line+=str(self.end.num)
                else:
                    buf=self.start
                    while(pos>1):
                        pos-=1
                        buf=buf.next
                    line+=str(buf.num)
            print(line)
                              

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
        L.addstart(elem)
        num=int(num/10)
    return L

            
L=Spisok()
t=0
while(t!=7):
    print("Выберете, что хотите сделать со списком(введите номер пункта):\n",
          "1)Добавить элемент/создать список\n",
          "2)Удалить элемент\n","3)Удалить список\n",
          "4)Найти элемент в списке\n",
          "5)Найти элемент, стоящий на определенной позиции\n",
          "6)Функция записи числа по разрядам в виде списка\n",
          "7)Завершить работу")
    t=int(input())
    b=1
    if(t==1):
        s=int(input("Введите количество элементов,которые вы хотите добавить:"))
        while(s>0)and b:
            s-=1
            pos=int(input("Введите позицию для добавления элемента:"))
            elem=int(input("Введите значение:"))
            b=L.addin(elem,pos)
    if(t==2):
        pos=int(input("Введите позицию удаляемого элемента:"))
        L.delin(pos)
    if(t==3):
        L=Spisok()
    if(t==4):
        elem=int(input("Введите элемент:"))
        L.search(elem)
    if(t==5):
        pos=int(input("ведите позицию:"))
        L.find(pos)
    if(t==6):
        num=int(input("Введите число:"))
        L=putnum(num)
    L.printsp()
L=None
        
        
