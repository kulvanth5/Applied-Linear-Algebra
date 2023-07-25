import sys

def matrix_create(n):

	matrix = []

	for i in range(0,n):

		temp = []

		for j in range(0,n):

			print('enter',i,j,'th value')
			temp.append(int(input()))

		matrix.append(temp)

	return matrix



def subMatrix(r,c,m):

	sm = []

	for i in range(0,len(m)):
	
		temp = []
	
		if i != r:
		
			for j in range(0,len(m[0])):
			
				if j != c:
					
					temp.append(m[i][j])
					
			sm.append(temp)
					
	return sm
	
def det(m):

	if len(m) == 1:
		return m[0][0]

	if len(m) == 2:
		return m[0][0]*m[1][1] - m[0][1]*m[1][0]
		
	ans = 0
	
	for i in range(len(m)):
	
		sm = subMatrix(0,i,m)
		ans = ans + pow(-1,0+i)*m[0][i]*det(sm)
		
	return ans	


def adjoint(m):

	adjoint = []

	for i in range(len(m)):
	
		temp = []
	
		for j in range(len(m)):
		
			sm = subMatrix(j,i,m)
			prod = det(sm)
			temp.append(pow(-1,i+j)*prod)
			
		adjoint.append(temp)

	print('adjoint of given matrix is ',adjoint)
		
	return adjoint
		
n = int(input('Enter the order of the matrix'))

if n <= 0:
	print('Invalid input')
	sys.exit()
	
m = matrix_create(n)

determinant = det(m)

m = adjoint(m)

print('det of matrix is ',determinant)

if determinant != 0.0:
	
	determinant = 1/determinant
	
	for i in range(len(m)):
	
		for j in range(len(m)):
			m[i][j] = float(m[i][j])*determinant
			
	print('inverse of given matrix is',m)
	
else:
	print('Given matrix does not have inverse')



