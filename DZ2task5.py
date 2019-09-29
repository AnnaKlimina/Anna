class Graf:
    def __init__(self,s):
        self.pr=[]
        self.last=0
        self.M=[[-1 for y in range(100)]for x in range(100)]
        self.W=[1000 for y in range(100)]
        self.F=[[False for y in range(100)] for x in range(100)]
        self.s=set([])
        self.sum=0
        self.N=0
        for i in range(len(s)):
            self.M[s[i][0]][s[i][1]]=s[i][2]
            self.M[s[i][1]][s[i][0]]=s[i][2]
            if (self.N<s[i][1]):
                self.N=s[i][1]
            if (self.N<s[i][0]):
                self.N=s[i][0]
            self.s.add(s[i][0])
            self.s.add(s[i][1])


    def ShortWay(self,start,end,k=0):
        for i in range(len(self.s)):
            m=1000
            point=-1
            for j in (self.s-{start}):
                if (start!=end)and(self.M[start][j]+self.last<self.W[j])and(self.M[start][j]>=0)and(self.F[start][j]!=True):
                    self.W[j]=self.M[start][j]+self.last
                if (start!=end)and(m>self.M[start][j]) and (self.F[start][j]!=True) and(self.M[start][j]>=0):
                    m=self.M[start][j]
                    point=j
            if (point!=-1):
                self.last=self.W[point]
                self.F[start][point]=True
                self.F[point][start]=True
                self.ShortWay(point,end,k+1)
        if(k==0):
            self.pr.insert(0,end)
            self.printW(start,end)
            self.pr.insert(0,start)
            print("Путь:",self.pr)

    def printW(self,start,end):
        for j in (self.s-{end}):
            if(self.W[end]-self.M[end][j]==self.W[j])and(self.M[end][j]>=0):
                self.pr.insert(0,j)
                self.printW(start,j)
                break


s=eval(input("Введите массив рёбер:\n"))
G=Graf(s)
b=int(input("Введите стартовую точку - "))
e=int(input("Введите конечную точку - "))
G.ShortWay(b,e)
