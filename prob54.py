class hand:
    def __init__(self,li):
        cards=[]
        for i in li:
            cards.append(i)
        suitIndex=list('SDHC')
        self.suits=[0 for i in xrange(4)]
        rankIndex=list('23456789TJQKA')
        self.ranks=[0 for i in xrange(13)]
        for card in cards:
            self.suits[suitIndex.index(card[1])]+=1
            self.ranks[rankIndex.index(card[0])]+=1
        self.getHandType()
        print li,self.handvalue
    def getHandType(self):
        i=0
        htype=''
        if 5 in self.suits:
            if self.ranks!=[0 for i in xrange(8)]+[1 for i in xrange(5)]:
                htype='royal'
            else:
                for i in xrange(8):
                    if self.ranks[i:i+5]==[1 for i in xrange(5)]:
                        htype='sflush'+str(i)
                if htype!='sflush':htype='flush'+str(self.ranks.index('1'))
        elif 4 in self.ranks:htype='fok'+str(self.ranks.index(4))
        elif 3 in self.ranks and 2 in self.ranks:htype='fhouse'+str(self.ranks.index(3))+str(self.ranks.index(2))
        elif 3 in self.ranks:htype='thok'+str(self.ranks.index(3))
        elif 2 in self.ranks:
            if self.ranks.count(2)==2:
                htype='tok'+str(self.ranks.index(2))+str(13-[i for i in reversed(self.ranks)].index(2))
            else:
                htype='pair'+str(self.ranks.index(2))
        else:
            self.ranks.reverse()
            htype=str(13-self.ranks.index(1))
        self.handvalue=htype
    def __cmp__(self,h2):
        return self.handvalue>h2.handvalue
        
infile = open('poker.txt')
sums=0
for line in infile:
    game=line.split()
    h1=hand(game[0:5])
    h2=hand(game[5:])
    if h1>h2:sums+=1
infile.close()
print sums
