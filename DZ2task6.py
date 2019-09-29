
class Graf:
    def __init__(self,s,N):
        self.l=N+1
        self.pr=[]
        self.M=[[-1 for y in range(N+1)]for x in range(N+1)]
        self.W=[10000 for y in range(N+1)]
        self.F=[[False for y in range(N+1)] for x in range(N+1)]
        self.all=set([])
        self.s=set([])
        for i in range(len(s)):
            self.M[s[i][0]][s[i][1]]=s[i][2]
            self.all.add(s[i][0])
            self.all.add(s[i][1])



    def Signal(self,start,p=0,k=0):
        m=-1
        self.s.add(start)
        for i in range(self.l):
            for j in (self.all-{start}):
                if (self.M[start][j]+p<self.W[j])and(self.M[start][j]>=0)and(self.F[start][j]!=True):
                    self.W[j]=self.M[start][j]+p
                    self.F[start][j]=True
                    self.Signal(j,self.W[j],k+1)
        if(self.s==self.all)and(k==0):
            for j in range (self.l):
                if(m<self.W[j])and(self.W[j]<10000):
                    m=self.W[j]
        return(m)
        
            
                



s=eval(input("Введите массив рёбер:\n"))
N=int(input("Введите размерность:"))
G=Graf(s,N)
b=int(input("Введите стартовую точку - "))
N=G.Signal(b)
print(N)
