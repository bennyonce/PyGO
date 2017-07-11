"""Sample"""
caster = ["A","B","C",["a","b","c",["aa","bb","cc"]]]
print("Hello")

"""Test Def 2017-06-28"""
def pygog(the_item):
	for each_item in the_item:
		if isinstance(each_item,list):
			pygog(each_item)
		else:
			print(each_item)


"""Test range 2017-07-03"""
def pygogp(the_item,level):
	for each_item in the_item:
		if isinstance(each_item,list):
			pygogp(each_item,level+1)
		else:
			for tab_stop in range(level):
				print("\t",end='')
			print(each_item)


"""Test indent 2017-07-04"""
def pygogpp(the_item,indent=False,level=0):
	for each_item in the_item:
		if isinstance(each_item,list):
			pygogpp(each_item,indent,level+1)
		else:
			ifindent:
				for tab_stop in range(level):
					print("\t",end='')
			print(each_item)

"""Test std out to file 2017-07-11"""
def pygof(the_item,indent=False,level=0,fh=sys.stdout):
	for each_item in the_item:
		if isinstance(each_item,list):
			pygof(each_item,indent,level+1,fh)
		else:
			if indent:
				for tab_stop in range(level):
					print('\t', end = '', file = fh)
			print(each_item, file = fh)