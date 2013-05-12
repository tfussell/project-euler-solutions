from math import cos,sin,radians,sqrt,atan,degrees,pi
import psyco
psyco.full()
def convert_angle(s,n):
    return [cos(radians(180.0/n*(2*s-1))),sin(radians(180.0/n*(2*s-1)))]
def surrounding_points(tn,a):
    angles=[[180.0/tn*(2*i-1)]+convert_angle(i,tn) for i in xrange(1,tn+1)]
    for i,j in enumerate(angles):
        if a<angles[i][0] and a>angles[i-1][0]%360:return [angles[i-1],angles[i]]
    else:
        return [angles[-1],angles[0]]
def angle(x,y):
    if x>0 and y>=0:return atan(y/float(x))
    elif x>0 and y<0:return atan(y/float(x))+2*pi
    elif x<0:return atan(y/float(x))+pi
    elif not x and y>0:return pi/2.0
    elif not x and y<0:return 3*pi/2.0
def minkowski_sum(poly_list):
    temp_polygon=poly_list[0]
    summed_polygon=[]
    for i in poly_list[1:]:
        for j in xrange(1,temp_polygon[0]+1):
            print i,surrounding_points(i,temp_polygon[1])
    return len(summed_polygon)
class Point:
    def __init__(self,a,x,y):
        self.x=x
        self.y=y
        self.angle=a
    def __str__(self):
        return "%s,%s,%s"%(self.angle,self.x,self.y)
class Polygon:
    def __init__(self,p):
        self.num_of_sides=p.pop(0)
        self.set_of_points=[]
        for i in p[0]:
            a,x,y=tuple(i)
            self.set_of_points.append(Point(a,x,y))
    def __str__(self):
        out=str(self.num_of_sides)+" "
        for i in set_of_points:
            out.append(i.__str__()+"\n")
        return out
def combine(*seqin):
    '''returns a list of all combinations of argument sequences.
for example: combine((1,2),(3,4)) returns
[[1, 3], [1, 4], [2, 3], [2, 4]]'''
    def rloop(seqin,listout,comb):
        '''recursive looping function'''
        if seqin:                       # any more sequences to process?
            for item in seqin[0]:
                newcomb=comb+[item]     # add next item to current comb
                # call rloop w/ rem seqs, newcomb
                rloop(seqin[1:],listout,newcomb)
        else:                           # processing last sequence
            listout.append([comb[0][0]+comb[1][0],comb[0][1]+comb[1][1]])        # comb finished, add to list
    listout=[]                      # listout initialization
    rloop(seqin,listout,[])         # start recursive process
    return listout
def main():
    for i in combine([convert_angle(i,17) for i in xrange(1,17+1)],[convert_angle(i,18) for i in xrange(1,18+1)]):
        print i    
    a=[[tn,[[180.0/tn*(2*i-1)]+convert_angle(i,tn) for i in xrange(1,tn+1)]] for tn in range(17,18)]
main()
