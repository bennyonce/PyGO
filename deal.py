num2 = []
other = []
try:
	data = open('ska.txt')
	for each_line in data:
		try:
			(num,cont) = each_line.split(':',1)
			cont = cont.strip()
			print(num)
			if num == '2':
				num2.append(cont)
			else:
				other.append(cont)
		except ValueError:
			pass
	data.close()
except IOError:
	print('Data File Missing.')

print(num2)
print(other)