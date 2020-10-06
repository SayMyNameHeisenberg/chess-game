'''input
BBBSSC
6 4 1
1 2 3
4

'''
import sys,math
def check(t,nb,ns,nc,pb,ps,pc,rb,rs,rc,r):
	b = (t*rb)-nb
	c = (t*rc)-nc
	s = (t*rs)-ns
	amt = max(0,b*pb) + max(0,c*pc) + max(0,s*ps)
	# print(amt)
	return r-amt


res = sys.stdin.readline()
nb,ns,nc= map(int, sys.stdin.readline().split(' '))
pb,ps,pc= map(int, sys.stdin.readline().split(' '))
r = int(sys.stdin.readline())
rb = res.count('B')
rs = res.count('S')
rc = res.count('C')

# if (rb==0):
# 	pb=0
# 	nb=0
# if (rc==0):
# 	pc=0
# 	nc=0
# if (rs==0):
# 	ps=0
# 	ns=0
minn = 0
maxx = 10**13+1
mid = 0
while(maxx>minn):
	mid = minn+math.ceil((maxx-minn)/2)

	l = check(mid,nb,ns,nc,pb,ps,pc,rb,rs,rc,r)

	if (l<0):
		maxx = mid-1
	else:
		minn = mid
	# print(mid,'mid')	
z = check(mid,nb,ns,nc,pb,ps,pc,rb,rs,rc,r)
pri = (rb*pb+rc*pc+rs*ps)
# # print(pri,mid,z)
# if (z<0):
# 	q = math.ceil(abs(z)/pri)
# 	mid-=q
print(minn)