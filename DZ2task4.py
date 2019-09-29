class Graf:
    def __init__(self,s):
        self.sp=[]    
        #self.pr=[]    
        self.st=set([])    
        self.dic={}
        for j in range(len(s)):
            self.start=s[j][0]
            if not(s[j][0] in self.dic.keys()):
                self.dic[s[j][0]]={(s[j][1])}
            else:
                self.dic[s[j][0]].add(s[j][1])
            if not(s[j][1] in self.dic.keys()):
                self.dic[s[j][1]]={(s[j][0])}
            else:
                self.dic[s[j][1]].add(s[j][0])

    def printG(self):
        for j in self.dic.keys():
            print(j,':',self.dic[j])

    def DFS(self,point):
        self.st.add(point)
        print(point,end=" ")
        for j in self.dic[point]:
            if not(j in self.st):
                self.DNS(j)

    def BFS(self,point):
        self.st.add(point)
        print(point,end=" ")
        for j in self.dic[point]:
            if not(j in self.st):
                self.sp.append(j)
        if not(self.dic[point]<self.st):
            while(self.sp!=[]):
                j=self.sp.pop(0)
                if not(j in self.st):
                    self.BNS(j)
    

    def Clear(self):
        print()
        self.sp=[]    
        #self.pr=[]    
        self.st=set([])

        
s=eval(input("Введите массив рёбер:\n"))
G=Graf(s)
G.printG()
print("DNS:")
G.DNS(G.start)
G.Clear()
print("BNS:")
G.BNS(G.start)
    
