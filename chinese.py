def egcd(a, b):
	auxiliar = (a, b)
	a = max(auxiliar)
	b = min(auxiliar)
	x = (1, 0)
	y = (0, 1)
	while a % b != 0:
		q = a / b
		c = a % b
		nx = x[0] - (x[1] * q)
		ny = y[0] - (y[1] * q)
		x = (x[1], nx)
		y = (y[1], ny)
		a = b
		b = c
	resultado = (b, x[1], y[1])
	return resultado

def chinese():
	a = [4, 5, 6, 7, 8, 9]
	m = [2, 3, 5, 7, 11, 13]
	n = 1
	x = 0
	for i in m:
		n = n * i
	for i in xrange(0, len(m)):
		temporal = m[i]
		exgcd = egcd(temporal, n / temporal)
		e = exgcd[1] * (n / temporal)
		x += e * a[i]
	x = x + n
	print x
	
chinese()
