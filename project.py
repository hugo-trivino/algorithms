def getData(prob):
   f = open("./instances/instance" + str("0" + str(prob))[-2:] + ".txt",'r')
   centers = int(f.readline())
   C=[]
   P=[]
   for x in range(centers):
      y=f.readline()
      coor=y.split(" ")
      C.append([float(coor[0]),float(coor[1])])
      if  not y :
          break
   points=int(f.readline())
   for x in range(points):
      y=f.readline()
      coor=y.split(" ")
      P.append([float(coor[0]),float(coor[1])])
      if  not y :
          break 
   return [C,P]
def addBin(c,E):
   l=0
   r=len(E)-1
   if not E:
      E.append(c)
      return
   if c<E[l]:
      E.insert(l,c)
      return
   if c>E[r]:
      E.append(c)
      return
   while l<r:
      m =(l+r)/2
      if E[m]> c:
         r=m
      if l==r-1:
         if E[l]<c:
            E.insert(l+1,c)
            return
      elif E[m]<c:
         l=m
         if l==r-1:
            if E[r]>c:
               E.insert(r,c)
               return
      if E[m]==c or E[l]==c or E[r]==c:
         return
def rmvBin(c,E):
   l=0
   r=len(E)-1
   if not E:
      return
   if c<E[l]:
      return
   if c>E[r]:
      return
   while l<=r:
      m =(l+r)/2
      if E[m]==c:
         E.pop(m)
         return
      if E[l]==c:
         E.pop(l)
         return
      if E[r]==c:
         E.pop(r)
         return
      if E[m]> c:
         r=m
         if l==r-1:
            if E[l]<c:
               return
      elif E[m]<c:
         l=m
         if l==r-1:
            if E[r]>c:
               return
def dist(c,p):
   from math import sqrt
   return sqrt((c[0]-p[0])**2 + (c[1]-p[1])**2)

def greedy(instance,outputToFile=True):
    def addGreedyCenter(c):
        for p in P2C[c]:
            rmvBin(p,M)
        Q[c]=1
        addBin(c,S)
        rmvBin(c,R)

    C,P=getData(instance)
    P2C=[]
    Q=[0]*len(C)
    M=[]
    R=[]
    S=[]
    for c in range(len(C)):
        R.append(c)
        maxCover=[0,0]
        points=[]
        cover=0
        for p in range(len(P)):
            d=dist(C[c],P[p])
            if d <=1.0:
                points.append(p)
                cover+=1
        P2C.append(points)
        if cover>maxCover[1]:
            maxCover=[c,cover]
    for p in range(len(P)):
        M.append(p)      
    addGreedyCenter(maxCover[0])
    done=False
    while not done:
        maxCover=[0,0]
        for c in range(len(R)):
            cover=0
            for p in range(len(M)):
                d=dist(C[R[c]],P[M[p]])
                if d <=1.0:
                    cover+=1
            if cover>maxCover[1]:
                maxCover=[R[c],cover]
        if not maxCover[1]:
            done=True
        if not done:
            addGreedyCenter(maxCover[0])
    answer=[]
    for s in S:
        answer.append(s+1)
    if outputToFile:
        file = open("./solutions/greedy_solution"+str("0"+str(instance))[-2:]+".txt","w")
        file.write("greedy "+str(len(S))+"\r\n")
        for a in answer:
            file.write(str(a)+"\r\n")
        file.close()
    return answer

def local(instance,outputToFile=True):
    def isRemovable(c):
        for p in P2C[c]:
            if M[p]==1:
                return False
        return True
    def isFeasible(q1,q2,r):
        ls=[]
        i=0
        j=0
        while i < len(P2C[q1]) and j < len(P2C[q2]):
            if P2C[q1][i] < P2C[q2][j]:
                ls.append(P2C[q1][i])
                i+=1
            else:
                ls.append(P2C[q2][j])
                j+=1
        for x in range(i,len(P2C[q1])):
            ls.append(P2C[q1][x])
        for x in range(j,len(P2C[q2])):
            ls.append(P2C[q2][x])
        n=0
        for v in range(len(P2C[r])):
            for u in range(n,len(ls)):
                if u>=len(ls):
                    break
                if P2C[r][v]==ls[u]:
                    ls.pop(u)
                else:
                    if P2C[r][v]<ls[u]:
                        break
                    n+=1
        x=0
        while x < len(ls):
            t = ls[x]
            j=1
            x+=1
            while x <len(ls)  and t == ls[x]:
                x+=1
                j=j+1
            if M[t]<=j:
                return False
        return True      
    def removeCenter(c):
        for p in P2C[c]:
            M[p]-=1
        Q[c]=0
        rmvBin(c,S)
        addBin(c,R)
    def addCenter(c):
        for p in P2C[c]:
            M[p]+=1
        Q[c]=1
        addBin(c,S)
        rmvBin(c,R)
    def addBin(c,E):
        l=0
        r=len(E)-1
        if not E:
            E.append(c)
            return
        if c<E[l]:
            E.insert(l,c)
            return
        if c>E[r]:
            E.append(c)
            return
        while l<r:
            m =(l+r)/2
            if E[m]> c:
                r=m
                if l==r-1:
                    if E[l]<c:
                        E.insert(l+1,c)
                        return
            elif E[m]<c:
                l=m
                if l==r-1:
                    if E[r]>c:
                        E.insert(r,c)
                        return
            if E[m]==c or E[l]==c or E[r]==c:
                return
    def rmvBin(c,E):
        l=0
        r=len(E)-1
        if not E:
            return
        if c<E[l]:
            return
        if c>E[r]:
            return
        while l<=r:
            m =(l+r)/2
            if E[m]==c:
                E.pop(m)
                return
            if E[l]==c:
                E.pop(l)
                return
            if E[r]==c:
                E.pop(r)
                return
            if E[m]> c:
                r=m
                if l==r-1:
                    if E[l]<c:
                        return
            elif E[m]<c:
                l=m
                if l==r-1:
                    if E[r]>c:
                        return
    C,P=getData(instance)
    P2C=[]
    Q=[1]*len(C)
    M=[0]*len(P)
    R=[]
    S=[]
    for c in range(len(C)):
        points=[]
        for p in range(len(P)):
            d=dist(C[c],P[p])
            if d <=1.0:
                points.append(p)
        P2C.append(points)
        addCenter(c)
    for c in range(len(C)):
        if isRemovable(c):
            removeCenter(c)
            break
    local_optimal=False
    while not local_optimal:
        done=True
        for x in range(len(S)-1):
            for y in range(x+1,len(S)):
                for z in range(len(R)):
                    rtn = isFeasible(S[x],S[y],R[z])
                    if rtn:
                        c1,c2,r1=S[x],S[y],R[z]
                        done=False
                        break
                if not done:
                    break
            if not done:
                break
        if not done:
            removeCenter(c1)
            removeCenter(c2)
            addCenter(r1)
        if done:
            local_optimal=True
    for s in range(len(S)):
        if isRemovable(S[s]):
            removeCenter(S[s])
            break
    answer=[]
    for s in S:
        answer.append(s+1)
    if outputToFile:
        file = open("./solutions/local_solution"+str("0"+str(instance))[-2:]+".txt","w")
        file.write("local "+str(len(S))+"\r\n")
        for a in answer:
            file.write(str(a)+"\r\n")
        file.close()
    return answer
