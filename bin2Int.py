def bin2Dec(n):
	n = str(n)
	ans = 0
	c = len(n) - 1
	for i in n:
		ans += int(i)*2**c
		c -= 1
	return ans
##test
binary = 10100
print(bin2Dec(binary))
