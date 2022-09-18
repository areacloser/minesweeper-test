from random import randint
mp = [[0 for _ in range(10)] for _ in range(10)]
minepos = []

def primp():
	for i in mp:
		for j in i:
			print(j,end="\t")
		print("\n\n\n")

exp = 0
while exp < 15:
	a = randint(0,9)
	b = randint(0,9)
	if mp[a][b] == 0:
		mp[a][b] = -1
		minepos.append([a, b])
		exp += 1	

for i, j in minepos:
	for a in range(i-1, i+2):
		for b in range(j-1,j+2):
			if a >= 0 and a < 10 and b >=0 and b < 10:
				if mp[a][b] != -1:
					mp[a][b] += 1
		
def visit(m,n):
	if mp[m][n] == 0:
		mp[m][n] = 9
		if m+1 >= 0 and m+1 < 10 and mp[m+1][n] == 0:
			visit(m+1, n)
		if m-1 >= 0 and m-1 < 10 and mp[m-1][n] == 0:
			visit(m-1, n)
		if n+1 >= 0 and n+1 < 10 and mp[m][n+1] == 0:
			visit(m, n+1)
		if n-1 >= 0 and n-1 < 10 and mp[m][n-1] == 0:
			visit(m, n-1)
			
primp()
pos = input("Discover:").split()
print("\n\n\n")
visit(int(pos[0]), int(pos[1]))
primp()
