def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins,secs) = time_string.split(splitter)
	return(mins + '.' + secs)

def get_score(score_file):
	try:
		with open(score_file) as f:
			data = f.readline()
			return(data.strip().split(','))
	except IOError as err:
		print('File Error' + str(err))
		return(None)

print(sorted(set([sanitize(t) for t in get_score('james.txt')]))[0:3])
print(sorted(set([sanitize(t) for t in get_score('julie.txt')]))[0:3])
print(sorted(set([sanitize(t) for t in get_score('mikey.txt')]))[0:3])
print(sorted(set([sanitize(t) for t in get_score('sarah.txt')]))[0:3])


sarah_d = get_score('sarah2.txt')

sarah_data = {}
sarah_data['Name'] = sarah_d.pop(0)
sarah_data['DOB'] = sarah_d.pop(0)
sarah_data['Times'] = sarah_d

print(sarah_data['Name'] + "'s fastest times are:" +
str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))


"""Get dict func int""" 
def get_dict(score_file):     
	try:         
		with open(score_file) as f:             
			data = f.readline()             
			templ =data.strip().split(',') 
			return({'Name':templ.pop(0),'DOB':templ.pop(0),'Times':str(sorted(set([sanitize(t) for t in templ]))[0:3])})     
	except IOError as err:         
			print('File Error' + str(err))         
			return(None)

sarah_dict = get_dict('sarah2.txt')

print(sarah_dict['Name'] + "'s fastest times are:" + sarah_dict['Times'])


