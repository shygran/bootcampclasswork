x = 17391
h = 546
d = 943

if x%17 < h%17 and x%17 < d%17:
	print(x%17)
elif h%17 < x%17 and h%17 < d%17:
	print(h%17)
elif d%17 < x%17 and d%17 < h%17:
	print(d%17)
