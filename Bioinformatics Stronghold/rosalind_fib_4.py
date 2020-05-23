def rabbit(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return (rabbit(n-1)+(rabbit(n-2)*k))

n, k = map(int, input().split())

res = rabbit(n)
print(res)