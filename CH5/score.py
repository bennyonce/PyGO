with open('james.txt') as jaf:
	data = jaf.readline()
	james = data.strip().split(',')
with open('julie.txt') as juf:
	data = juf.readline()
	julie = data.strip().split(',')
with open('mikey.txt') as mif:
	data = mif.readline()
	mikey = data.strip().split(',')
with open('sarah.txt') as saf:
	data = saf.readline()
	sarah = data.strip().split(',')

def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins,secs) = time_string.split(splitter)
	return(mins + '.' + secs)

james_c = []
julie_c = []
mikey_c = []
sarah_c = []

"""初始版本
for each_t in james:
	james_c.append(sanitize(each_t))
for each_t in julie:
	julie_c.append(sanitize(each_t))
for each_t in mikey:
	mikey_c.append(sanitize(each_t))
for each_t in sarah:
	sarah_c.append(sanitize(each_t))

print(sorted(james_c))
print(sorted(julie_c))
print(sorted(mikey_c))
print(sorted(sarah_c))
"""

"""列表推导 2017-07-11"""
print(sorted([sanitize(t) for t in james]))
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in mikey]))
print(sorted([sanitize(t) for t in sarah]))