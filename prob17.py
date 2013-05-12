lengths=dict([
['1',3],['11',6],['10',3],['2',3],['12',6],['20',6],['3',5],['13',8],['30',6],
['4',4],['14',8],['40',5],['5',4],['15',7],['50',5],['6',3],['16',7],['60',5],
['7',5],['17',9],['70',7],['8',5],['18',8],['80',6],['9',4],['19',8],['90',6]])
def letters_in(i):
    if str(i) in lengths:return lengths[str(i)]
    else:
        if i>20 and i<100:return lengths[str(i)[0]+'0']+letters_in(int(str(i)[1]))
        elif i==1000:return 11
        elif i%100==0:return lengths[str(i)[0]]+7
        else:return lengths[str(i)[0]]+10+letters_in(int(str(i)[1:3]))
total_letters=0
for i in xrange(1,1001):total_letters+=letters_in(i)
print total_letters
