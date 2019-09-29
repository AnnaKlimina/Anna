
class GrafOrlov:
    def __init__(self,s):
        self.last=[]
        self.pr=[]
        self.sp=set([])
        self.dic={}
        for j in range(len(s)):    
                if not(s[j][0] in self.dic.keys()):                   
                    self.dic[s[j][0]]=[1000,{s[j][1]},[s[j][1],s[j][2],0]]                   
                else:
                    self.dic[s[j][0]].append([s[j][1],s[j][2],0])
                    self.dic[s[j][0]][1].add(s[j][1])
                if not(s[j][1] in self.dic.keys()):
                    self.dic[s[j][1]]=[1000,{s[j][0]},[s[j][0],s[j][2],0]]
                else:
                    self.dic[s[j][1]].append([s[j][0],s[j][2],0])
                    self.dic[s[j][1]][1].add(s[j][0])

    def printG(self):
        for j in self.dic.keys():
            print(j,':',self.dic[j])
            

    def ShortWay(self,start,end,k=0):
        self.sp.add(start)    
        while not(self.dic[start][1]<=self.sp)and(start!=end):
            self.printG()
            print("dc")
            m=10000
            for j in range(2,len(self.dic[start])):
                print(start)
                if (self.dic[start][j][1]<=m) and (self.dic[start][j][2]!=1):
                    m=self.dic[start][j][1]
                    b=j
                    self.last=self.dic[start][j]
            if (m!=10000)and(start!=end):
                self.dic[self.last[0]][0]=m+self.dic[start][0]
                self.dic[start][b][2]=1
                for j in range(2,len(self.dic[self.last[0]])):
                    if (self.dic[self.last[0]][j][1]==start):
                        self.dic[self.last[0]][j][2]=1
                        break                   
                self.dic[self.last[0]]
                self.ShortWay(self.last[0],end,k+1)
                self.printG()
        if(self.dic.keys()==self.sp) and (k==0):
            self.printG()
            self.pr.insert(0,end)
            self.printShort(start,end)
            print("Длина пути-",self.dic[end][0]-1000,'\n',"Путь:")
            for j in range(len(self.pr)):
                print(self.pr[j],end=' ')
                


    def printShort(self,start,end):
        for j in range(2,len(self.dic[end])):
            if((self.dic[end][0]-self.dic[self.dic[end][j][0]][0])==self.dic[end][j][1]):
                self.pr.insert(0,self.dic[end][j][0])
                self.printShort(start,self.dic[end][j][0])
                break
        
                
            
        
s=eval(input("Введите массив рёбер:\n"))
G=GrafOrlov(s)
G.printG()
b=int(input("Введите стартовую точку - "))
e=int(input("Введите конечную точку - "))
G.ShortWay(b,e)

