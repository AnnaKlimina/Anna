def fu(buf,s,i,sp):
    if (i<len(s)):
        for j in(dic[s[i]]):
            if (buf==None):
                buf=""
            buf+=j
            fu(buf,s,i+1,sp)
            buf=buf[0:len(buf)-1]
    else:
        sp.add(buf)
        buf=buf[0:len(buf)-1]
        return buf
        
        
dic={"2":"abc","3":"def",
     "4":"ghi","5":"jkl",
     "6":"mno","7":"pqrs",
     "8":"tuv","9":"wxyz",
     "0":" ","1":"./,"}
sp=set([])
s=str(input("Введите последовательность цифр:\n"))
buf=""
i=0
fu(buf,s,i,sp)
print(sp,len(sp))
    
    
