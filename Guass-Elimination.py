import sys

def matrix_create(n):

	matrix = []

	for i in range(0,n):
		
		temp = list(map(int,input('Enter co-efficients and constant of eqn {} : '.format(i)).split()))
		matrix.append(temp)

	return matrix

def reduce(x,y,index):

	alpha = y[index]/x[index]

	for i in range(len(x)):
		y[i] = y[i] - (alpha*x[i])

	return y

n = int(input('Enter the no.of variables and eqns'))

if n <= 0:
	print('Invalid input')
	sys.exit()
	
m = matrix_create(n)
j = 0
agu_rank = 0

def check_pivot(m,i):
	
	temp = i

	while m[temp][i] == 0.0 and temp < (len(m)-1):
		print(temp)
		temp = temp + 1

	if m[temp][i] != 0.0:
		change_row = m[i]
		m[i] = m[temp]
		m[temp] = change_row 

	return m
	
while j < len(m):

	m = check_pivot(m,j)

	if m[j][j] != 0.0:
		agu_rank += 1
		for i in range(j+1,len(m)):
			m[i] = reduce(m[j],m[i],j)

	j = j+1

print('rank of the agumented matrix is',agu_rank)
print('reduced matrix is',m)

cfm = m
rank = 0
i = 0
cofs = []

for i in range(len(cfm)):
	cofs.append(cfm[i].pop())
	# print(i)
	if cfm[i][i] != 0.0:
		rank = rank + 1

print('Rank of co-efficient matrix is ',rank)
#print('cofs is',cofs)

if rank == agu_rank and rank < n:
	print('The system has infinitely many solutions')

elif rank < agu_rank:
	print('The system is inconsistent')

else:

	def evaluate(cf,vals,index,rhs):

		print(cf,vals,rhs)
		factor = 0
		for i in range(index+1,len(cf)):
			factor = factor + cf[i]*vals[i]

		ans = (rhs-factor)/cf[index]
		print(ans)
		return ans

	soln = [ 0 for i in range(len(cfm))]

	for j in range(len(cfm)-1,-1,-1):

		cf = cfm[j]
		soln[j] = evaluate(cf,soln,j,cofs[j])
		i = i+1


	print('The solution of given system is ',soln)



