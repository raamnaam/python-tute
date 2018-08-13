
def function(n):
	def forword(n,x,y):
		if x == y:
			return n
		i = n[y]

		if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
			backword(n,x,y)

		else:
			x += 1
			forword(n,x,y)

	def backword(n,x,y):
		j = n[y]
		if x == y:
			return n
		if (j=='a' or j=='e' or j=='i' or j=='o' or j=='u' or j=='A' or j=='E' or j=='I' or j=='O' or j=='U'):
			z = n[y]
			n[y] = n[x]
			n[x] = z
			y -= 1
			x += 1
			forword(n,x,y)

		else:
			y -= 1
			backword(n,x,y)


	n = list(n)
	x = 0
	y = len(n)-1
	print(''.join(n))

function("it's all done....!")













