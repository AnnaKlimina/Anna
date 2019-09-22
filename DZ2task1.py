p=int(input("Поиск подстроки в строке. Нажмите:\n'1'-начать работу с программой\n'2'-завершить работу\n"))
while(p==1):
    s=str(input("Введите строку: "))
    m=0
    l=len(s)/2
    i=len(s)//l
    while (l>0):
        if(i*l==len(s)):
            l=int(l)
            i=int(i)
            k=0
            f=1
            t=s[0:l]
            for j in range(i):
                if (t==s[l*(j):l*(j+1)]):
                    k+=1
                else:
                    f=0
                    break
            if(k>m) and f:
                m=k
                buf=t
        l-=1
        if(l>0):
            i=len(s)//l
    k=m
    if (k==0):
        print("Такой подстроки не существует")
    else:
        print(k,buf)
    p=int(input("Поиск подстроки в строке. Нажмите:\n'1'-начать работу с программой\n'2'-завершить работу\n"))        
        
    
