import time
import psyco
psyco.log('log.txt')
psyco.full()

def brickEdges(form,n):
    li = [0 for i in xrange(n)]
    index=-1
    for i in form:
        if i=='2':index+=2
        else:index+=3
        li[index]=1
    li.pop()
    return li     
def canComeAfter(a,b,n):
    can = True
    l2=brickEdges(b,n)
    l1=brickEdges(b,n)
    for i,j in zip(l1,l2):
        if i==j and i==1:can=False
    return can
def importPossibleRows(w,h):
    def permutate(n,threes):
        a=[0 for i in xrange(n)]
        li=[]
        while a!=[1]*n:
            f = []
            for i in a:
                if i==1:
                    f.append('2')
                else:
                    f.append('3')
            temp = ''.join(f)
            if temp.count('3')==threes and temp not in li:
                li.append(temp)
            added=False
            ind=len(a)-1
            while not added and ind>=0:
                if a[ind]==0:
                    a[ind]=1
                    added=True
                else:
                    a[ind]=0
                    ind-=1
        f = []
        for i in a:
            if i==1:
                f.append('2')
            else:
                f.append('3')
        temp = ''.join(f)
        if temp.count('3')==threes and temp not in li:
            li.append(temp)
        return li
    def blocksInLength(n):
        p = []
        for i in xrange(n):
            for j in xrange(n):
                if i*2+j*3==n:p.append([i,j])
        return p
    output=[]
    for i in blocksInLength(w):
        for j in permutate(sum(i),i[1]):
            output.append(j)
    return output
def generateRowHashTable(possibleRows,w):
    def getType(a):
        if a[0]=='2' and a[-1]=='2':type=0
        elif a[0]=='2' and a[-1]=='3':type=1
        elif a[0]=='3' and a[-1]=='2':type=2
        else:type=3
        return type
    possibleRowsDict = {}
    types = [[] for i in xrange(4)]
    for i in possibleRows:
        types[getType(i)].append(i)
    start = time.time()
    print 'Compiling...'
    for i in possibleRows:
        possibleNextRows=types[3-getType(i)]
        tempList = []
        for j in possibleNextRows:
            if canComeAfter(i,j,w):tempList.append(j)
        possibleRowsDict[i]=tempList
    print 'Done'
    print time.time()-start
    return possibleRowsDict
def buildWalls(rDict,perms,h):
    gWalls=0
    globalHashTable = {}
    print 'Building crackless walls...'
    for p in perms:
        globalHashTable[p+'x1'] = 1
    for i in xrange(2,h+1):
        for p in perms:
            globalHashTable[p+'x%s'%i]=0
            for k in rDict[p]:
                globalHashTable[p+'x%s'%i]+=globalHashTable[k+'x%s'%(i-1)]
    for p in perms:
        gWalls+=globalHashTable[p+'x%s'%(h)]
    return gWalls
def main():
    w,h=32,10
    possible = importPossibleRows(w,h)
    dictionaryOfRows = generateRowHashTable(possible,w)
    gWalls = buildWalls(dictionaryOfRows,possible,h)
    print "W(%s,%s) = %s"%(w,h,gWalls)

if __name__=="__main__":
    main()
