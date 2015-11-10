def check_for_string(input):
	if type(input) == str:
		print 'Its a string'
	else:
		print 'Its not a string'

def check_for_string(input):
	if type(input) == str:
		print input, 'is a string'
	else:
		print input, 'is not a string'

check_for_string('hello')
check_for_string(True)

def larger (num1, num2):
	if num1 > num2:
		return num1
	else:
		return num2
print larger (4, 8)