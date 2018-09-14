# tiempo: 0.0687 segundos

def euler4(s):	
	a = 999
	c = 999
	while (a > 900):
		for x in s:
			if (x % a == 0):
				return a
			else:
				a -= 1

	 	
def palindromos():
	a = 998001
	z = 900000
	s = [] 
	while (z < a):
		p = str(z)
		if (p == p[::-1]):
			n = int(p)
			s.append(n)
		z = z + 1
	return s

s = palindromos()
print (euler4(s)) 
