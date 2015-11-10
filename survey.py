#print "Welcome to the survey!"
name = raw_input ("What is your name? ")

color = raw_input ("What is your fav color? ")

hobby = raw_input ("What is your fav hobby? ")

movie = raw_input ("What is your fav movie? ")

eye = raw_input ("What is your eye color? ")

height = raw_input ("What is your height? ")

#print name + "'s favorite color is", color
#print name + "'s favorite hobby is", hobby
#print name + "'s", "favorite movie is", movie

def print_survey_results (name, color, hobby, movie, eye, height):
	print name + "'s favorite color is " + color
	print "%s's favorite hobby is %s." % (name, hobby)
	print name + "'s favorite movie is " + movie
	print name + "'s eye color is " + eye
	print name + "'s height is " + height
print_survey_results (name, color, hobby, movie, eye, height)