import sys

num2 = []
other = []
try:
	data = open('ska.txt')
	for each_line in data:
		try:
			(num,cont) = each_line.split(':',1)
			cont = cont.strip()
			"""print(num)"""
			if num == '2':
				num2.append(cont)
			else:
				other.append(cont)
		except ValueError:
			pass
	data.close()
except IOError:
	print('Data File Missing.')

"""
print('Numeber 2 content:',num2)
print('Other content',other)

try:
	num_file = open('num_data.txt','w')
	other_file = open('other_data.txt','w')

	print(num2, file = num_file)
	print(other, file = other_file)

except IOError as err:
	print('File Error' + str(err))

finally
	num_file.close()
	other_file.close()

	"""

"""Method 2 using 'with' """
try:
	with open('num_data.txt','w') as num_file:
		print(num2, file = num_file)
	with open('other_data.txt','w') as other_file:
		print(other, file = other_file)

except IOError as err:
	print('File Error' + str(err))



"""Method 2 using 'with' and split with 'pygof' """
def pygof(the_item,indent=False,level=0,fh=sys.stdout):
	for each_item in the_item:
		if isinstance(each_item,list):
			pygof(each_item,indent,level+1,fh)
		else:
			if indent:
				for tab_stop in range(level):
					print('\t', end = '', file = fh)
			print(each_item, file = fh)

try:
	with open('num_data.txt','w') as num_file:
		pygof(num2, fh = num_file) 
		"""只需要提供必要的参数，带上参数名"""
	with open('other_data.txt','w') as other_file:
		pygof(other, fh = other_file)

except IOError as err:
	print('File Error' + str(err))


