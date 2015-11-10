my_name = 'Paul'
my_partners_name = 'Rachel'
my_age = 19

if my_name > my_partners_name:
    print 'My name is greater'
elif my_name < my_partners_name:
    print 'Their name is greater'
else:
    print 'our names are equal!'

if 26 >= 15:
	print "Oh we're halfway there!"
else:
    print "The month is still young."

today = 'Tuesday'

if today == 'Monday':
    print 'Yay class day!'
elif today == 'Tuesday':
    print 'Sigh its only Tuesday'
elif today == 'Wednseday':
    print 'Humpday!'
elif today == 'Thursday':
    print '#tbt'
elif today == 'Friday':
    print 'TGIF'
else:
    print "Yeah, it's the weekend!"

if my_age >= 18:
	print "Yay! I can vote!"

if my_age >= 18:
	print "Yay! I can vote!"
else:
	print "Aww, I cannot vote."

if my_age >= 18 and my_age >= 21:
	print "I can vote and go to a bar!"

if my_age >= 21:
	print "I can go to a bar"
elif my_age >= 18 and my_age < 21:
	print "I can vote but I cannot go to a bar"
else:
	print "I cannot vote or go to a bar"

if 8 % 2 == 0:
	print "The number 8 is even."
else:
	print "The number 8 is odd."

if 8 % 2 != 0:
	print "The number 8 is odd"
else:
	print "The number 8 is even"

if 8 % 2 == 0 and 9 % 2 == 0:
	print "Both numbers are even."
else:
	print "Both numbers are not even."

if 8 % 2 == 0 and 9 % 2 == 0:
	print "Both numbers are even."
elif 8 % 2 == 0 and 9 % 2 != 0:
	print "8 is evan and 9 is odd."
elif 8 % 2 != 0 and 9 % 2 == 0:
	print "8 is odd and 9 is even."
else:
	print "Both numbers are odd."

my_favorite_color = "blue"

if my_favorite_color == "blue":
	print "My favorite color is blue!"
else:
	print "My favorite color is not blue."

if my_favorite_color == "blue" or "yellow" or "red":
	print "My favorite color is primary color"
else:
	print "My favorite color is a secondary color"