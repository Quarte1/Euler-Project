a = 0
b = 1

def fib():
	a, b = 1, 2
	while True:
		yield a
		a, b = b, a + b
f = fib()
cnt = 0
sum = 0
for i in f:
	if i < 4000000 and i%2 == 0:
		print i
		sum += i
	elif i > 4000000:
		break

	cnt += 1

print "!"
print "sum: ",sum