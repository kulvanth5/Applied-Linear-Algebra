m = [[-2,3,7,9],[10,-5,2,5],[-13,8,12,-20],[3,-33,6,-4]]

m1 = m
count = 0

def reduce(x,y,index):

	alpha = y[index]/x[index]

	for i in range(len(x)):
		y[i] = y[i] - (alpha*x[i])

	return y

j = 0

while j < len(m1[0]):

	if m1[j][j] != 0.0:
		count += 1
		for i in range(j+1,len(m1)):
			m1[i] = reduce(m1[j],m1[i],j)

	j = j+1

print('rank of the matrix is',count)


