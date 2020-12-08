def replace(lst, ins, s):
	occurrence = 0
	for row in range(len(lst)):
		if lst[row] == s:
			try:
				lst[row] = ins[occurrence%len(ins)]
				occurrence += 1
			except:
				pass
	return lst
