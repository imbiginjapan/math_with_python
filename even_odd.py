def even_odd(a):
	if a % 2 == 0:
		return 'Even'
	else:
		return 'Odd'

def vend(a,b):
	for i in range(1,b+1):
		print('{0} x {1} = {2}'.format(a, i, a*i))
	
if __name__ == '__main__':
	a = float(input ('Enter a Number: '))
	if a.is_integer():
		a = int(a)
		print(even_odd(a))
		b = float(input ('Enter Times to Multiply: '))	
		if b.is_integer():
			b = int(b)
			vend(a,b)
		else: 
			('Invalid value')
	else: 
		('Invalid value')

	
