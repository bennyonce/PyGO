def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins,secs) = time_string.strip().split(splitter)
	return(mins + '.' + secs)

class AthleteList(list):
	"""docstring for Athlete"""
	def __init__(self, a_name, a_dob = None, a_times = []):
		list.__init__([])
		self.name = a_name
		self.dob = a_dob
		self.extend(a_times)

	def top3(self):
		return(sorted(set([sanitize(t) for t in self]))[0:3])

	
		

def get_cls(score_file):     
	try:         
		with open(score_file) as f:             
			data = f.readline()             
			templ =data.strip().split(',') 
			return(Athlete(templ.pop(0),templ.pop(0),templ))     
	except IOError as err:         
			print('File Error' + str(err))         
			return(None)


vera = AthleteList('Vera Vi')
vera.append('1.31')
print("Vera's time1:" + str(vera.top3()))
vera.extend(['2.22','1-21','2:22'])
print("Vera's time3:" + str(vera.top3()))

sarah_cls = get_cls('sarah2.txt')

print(sarah_cls.name + "'s fastest times are:" + str(sarah_cls.top3()))
